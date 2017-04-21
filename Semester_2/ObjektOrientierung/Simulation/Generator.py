#!/usr/bin/env python3
# encoding=utf-8
import random
from men import men
from women import women
from matches import matches
import names
import math

lmatches = []


def create_humans(amount):
    humans = []
    for i in range(amount):
        if random.randint(0,2) == 0:
            humans.append(men(names.get_first_name(gender='male'),random.randint(20,55)))
        else:
            humans.append(women(names.get_first_name(gender='female'),random.randint(20,55), random.randint(0,2)))
    return humans


def match_maker(lmen, lwomen):
    existing_couples = []
    new_couples = []

    for man in lmen:
        #Match a woman

        if len(lwomen) == 0:
            break
        for woman in lwomen:
            #Match only if sixteen or older
            if math.fabs(man.get_age() - woman.get_age()) <= 10 and man.get_age()>16 and woman.get_age() > 16:
                #Check if couple doesnt exist

                if matches(man, woman) in lmatches:
                    #Only add new couples
                    existing_couples.append(matches(man, woman))
                else:
                    new_couples.append(matches(man, woman))
                lwomen.remove(woman)
                lmen.remove(man)
                break

    for lm in lmatches:
        if lm not in existing_couples:
            lmatches.remove(lm)
    for nc in new_couples:
        lmatches.append(nc)
    print("Existing couples " + str(len(existing_couples))+" Total: " +str(len(lmatches)))


def filter_by_gender(humans):
    l_men = []
    l_women = []

    for h in humans:

        if type(h) == men:
            l_men.append(h)
        else:
            l_women.append(h)
    return l_men, l_women


def print_statistic(humans):
    average_age = 0
    average_amount_kids = 0
    females = 0
    average_number_of_kids = 0
    for human in humans:
        average_age += human.get_age()
        #Count amount of babies
        if type(human) == women:
            females +=1
            average_amount_kids += human.get_kids()

    average_amount_kids = average_amount_kids / females
    average_age = average_age/len(humans)
    print("Average Age: "+str(int(average_age))+" Kids: " + str(normal_round(average_amount_kids)))

def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def simulate(humans):
    #they age
    for years in range(20):
        print("Simulating year: " +str(2017+years) + " Humans " + str(len(humans)))
        for h in humans:
            h.make_older()
            if h.die():
                humans.remove(h)

        men, women = filter_by_gender(humans)
        match_maker(men, women)

        for lm in lmatches:
            #Create new kids, old ones are still stored in the Couples class
            kids = lm.make_kids()
            if kids is not None:
                for kid in kids:
                    humans.append(kid)
        print_statistic(humans)
simulate(create_humans(2000))
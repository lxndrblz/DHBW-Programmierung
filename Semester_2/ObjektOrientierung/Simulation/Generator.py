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
            humans.append(men(names.get_first_name(gender='male'),random.randint(0,100)))
        else:
            humans.append(women(names.get_first_name(gender='female'),random.randint(0,100)))
    return humans


def match_maker(lmen, lwomen):
    existing_couples = []
    new_couples = []

    for man in lmen:
        #Match a woman

        if len(lwomen) == 0:
            break
        for woman in lwomen:
            if math.fabs(man.get_age() - woman.get_age()) <= 10:
                #Check if couple doesnt exist

                if matches(man, woman) in lmatches:
                    #Only add new couples
                    existing_couples.append(matches(man, woman))
                else:
                    new_couples.append(matches(man, woman))
                lwomen.remove(woman)
                lmen.remove(man)
                break

    print("existing couples " + str(len(existing_couples)))
    for lm in lmatches:
        if lm not in existing_couples:
            lmatches.remove(lm)
    for nc in new_couples:
        lmatches.append(nc)
    print("new couples " + str(len(new_couples)))


def sort_by_gender(humans):
    l_men = []
    l_women = []

    for h in humans:

        if type(h) ==men:
            l_men.append(h)
        else:
            l_women.append(h)
    return l_men, l_women


def simulate(humans):
    #they age
    for years in range(20):
        print("Simulating year: " +str(2017+years) + " Humans " + str(len(humans)))
        for h in humans:
            h.make_older()
            if h.die():
                humans.remove(h)

        men, women = sort_by_gender(humans)
        match_maker(men, women)

        for lm in lmatches:
            lm.make_kids()
            kids = lm.get_kids()
            for kid in kids:
                humans.append(kid)




simulate(create_humans(100))
#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import random
import itertools
from random import randint


def hashthis(s):
    h = 0
    base = 1
    for char in s:
        h += ord(char)*base
        base *= 26
    return h

#Funktion generiert Passwort mittels eines kartesischen Produktes aus dem Buchstabenarray
def bruteforcelinear(h):

    # Buchstaben in array umwandeln
    buchstaben = string.ascii_lowercase
    buchstabenarray = []
    for char in buchstaben:
        buchstabenarray.append(char)

    password = ''
    cartesianproduct = []
    # Anzahl an Stellen
    maxstellen = 5
    # ArgumentListe für cartesisches Produkt erzeugen
    for i in range(0, maxstellen):
        cartesianproduct.append(buchstabenarray)

    for pwcombinations in itertools.product(*cartesianproduct):
        # Jede Kombination prüfen
        for c in pwcombinations:
            password = password + str(c)
            if h == hashthis(password):
                return password
        password = ''

#Funktion generiert Passwort aus zufälligen Kombinationen
def bruteforce(h):
    buchstaben = string.ascii_lowercase
    
    while True:
        password = ''
        #Zufaellige Länge
        for i in range(randint(0,10)):
            #Zufaellige Buchstaben
            
            c = random.choice(buchstaben)
            password = password + c
        if(h == hashthis(password)):
            break
    return password

hashwert =hashthis(str(raw_input("Ihr Passwort: ")))
print "Hash Wert: " + str(hashwert)
print "Passwort war (zufall) verfahren " + str(bruteforce(hashwert))
print "Passwort war (linear) verfahren " + str(bruteforcelinear(hashwert))



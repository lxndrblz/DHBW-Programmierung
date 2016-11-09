#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

minGuess = 0
maxGuess = 20    
AnzahlVersuche = 0
ZahlErraten = False
print "Bitte überlegen Sie sich eine Zahl zwischen 1 und 20:"

while ZahlErraten == False:
    guess = (maxGuess +  minGuess) / 2
    print "Ist die Zahl? " + str(guess)
    print "Ist die Zahl (g)rößer, (k)leiner oder (r)ichtig?"
    auswahl = str(raw_input("Auswahl: "))
    if (auswahl.lower() == "g"):
        minGuess = guess
    if (auswahl.lower() == 'k'):
        maxGuess = guess
    if (auswahl.lower() == 'r'):
        ZahlErraten = True
    AnzahlVersuche += 1
print "Anzahl Versuche: " + str(AnzahlVersuche)
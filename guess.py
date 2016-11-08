#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
AnzahlVersuche = 1
ZufallsWert = randint(1,20)
print "Bitte eine Zahl zwischen 1 und 20 auswählen!"
guess = int(input("Ihr Tip: "))

while guess != ZufallsWert:
    AnzahlVersuche += 1
    if(guess>ZufallsWert):
        print "Zahl ist kleiner"
    else:
        print "Zahl ist größer"

    guess = int(input("Ihr neuer Tip: "))

print "Versuche: " + str(AnzahlVersuche)
#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
#Program zur Berechnung einer Fläche
print "Anwendung zur Berechnung einer Fläche"
print "Bitte eine Form auswählen: "
print "1 Rechteck"
print "2 Kreis"
#Auf gueltige Eingabe warten
formBerechnung = 0
while  True:
    formBerechnung =input("Ihre Auswahl: ")
    if formBerechnung == 1 or formBerechnung == 2:
        break
if formBerechnung == 1:
    #Rechteck berechnen
    Hoehe = input("Bitte Höhe eingeben: ")
    Breite = input("Bitte Breite eingeben: ")
    #Ausgabe
    print Hoehe*Breite
else:
    #Kreis berechnen
    radius = input("Bitte Radius eingeben: ")
    print radius*radius*math.pi
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Tannenbaum Python
anzahl_max = 7
#Zeilen des Tannebaums
for i in range (0,anzahl_max):
    reihe=""
    for sb in range (0, anzahl_max + (i+1)):
        #Leer Zeilen
        if sb  < ((anzahl_max - i)):
            reihe = reihe + " "
        else:
            reihe = reihe + "*"   
    print reihe

from random import randint

def zufaellige_wuerfe(anzahl):
    wuerfe = []
    for a in range(anzahl):
        augen = randint(1, 6)
        wuerfe.append(augen)
    return wuerfe


def anzahl_zufallszahl_a1o(anzahl):
    # Liste samt Wert indexieren
    zahlen = [0]*7
    for a in range(anzahl):
        augen = randint(1, 6)
        zahlen[augen] += 1
    return zahlen

def anzahl_zufallszahl(anzahl):
    wuerfe = zufaellige_wuerfe(anzahl)
    zahlen = []
    for w in range(0, 7):
        anzahl = wuerfe.count(w)
        zahlen.append(anzahl)
    return zahlen


augen = randint(1, 6)
print(augen)
print(zufaellige_wuerfe(20))
anzahl = anzahl_zufallszahl(1000)
print(anzahl)
print(anzahl[3])
anzahl = anzahl_zufallszahl_a1o(1000)
print(anzahl)
print(anzahl[3])

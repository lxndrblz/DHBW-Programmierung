import matplotlib.pyplot as plt
import numpy as np
from pkw import *


def autorennen(autolist):
    siegerliste = []
    while autolist:
        psProKg = autolist[0].leergewicht / autolist[0].leistung
        hoechste = autolist[0]
        for auto in autolist:
            psProKg2 = auto.leergewicht / auto.leistung
            if psProKg2 < psProKg:
                hoechste = auto
                psProKg = auto.leergewicht / auto.leistung
        if len(autolist) == 1:
            hoechste = autolist[0]
        index = autolist.index(hoechste)
        siegerliste.append(autolist.pop(index))

    return siegerliste


fahrzeug1 = pkw(1, 1000, 2000, 200, 200, 2)
fahrzeug2 = pkw(2, 1000, 2000, 200, 1990, 2)
fahrzeug3 = pkw(3, 1000, 2000, 200, 180, 2)
fahrzeug4 = pkw(4, 1000, 2000, 200, 1700, 2)

autoliste = [fahrzeug1, fahrzeug2, fahrzeug3, fahrzeug4]

gewinnerliste = autorennen(autoliste)

plt.axis([0, len(gewinnerliste) +1, 0, 10])
plt.xlabel('Platz')
plt.ylabel('PS pro KG')
plt.title('Autosimulation')
plt.ion()

for index, i in enumerate(reversed(gewinnerliste)):
    y = float(i.leergewicht / i.leistung)
    plt.annotate(i.fahrzeugnummer, xy=(index + 1, y), bbox=dict(boxstyle='circle,pad=0.5', fc='red', alpha=0.5))
    plt.pause(0.05)

while True:
    plt.pause(0.05)


plt.show()

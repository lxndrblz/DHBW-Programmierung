from fahrzeug import *

class Fahrrad(Fahrzeug):
    def __init__(self,fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht,rahmenhoehe):
        super().__init__(fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht)
        self.rahmenhoehe = rahmenhoehe
        self.leistung = 1

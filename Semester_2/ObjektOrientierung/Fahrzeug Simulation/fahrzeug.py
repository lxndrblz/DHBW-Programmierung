from random import random
class Fahrzeug():
    def __init__(self,fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht):
        self.fahrzeugnummer = fahrzeugnummer
        self.leergewicht = leergewicht
        self.zulaessigesGesamtgewicht = zulaessigesGesamtgewicht
        self.farbe = "Grundiert"

    def pruefeVerfuegbarkeit(self):
        return random() > 0.5

    def lackieren(self,farbe):
        self.farbe = farbe


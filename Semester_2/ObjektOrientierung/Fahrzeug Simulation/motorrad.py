from kraftfahrzeug import Kraftfahrzeug
class Motorrad(Kraftfahrzeug):
    def __init__(self,fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht,hoechstgeschwindigkeit,leistung):
        super().__init__(fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht,hoechstgeschwindigkeit,leistung)


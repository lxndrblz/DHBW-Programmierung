from kraftfahrzeug import Kraftfahrzeug
class lkw(Kraftfahrzeug):
    def __init__(self,fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht,hoechstgeschwindigkeit,leistung,nutzlast):
        super().__init__(fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht,hoechstgeschwindigkeit,leistung)
        self.nutzlast = nutzlast

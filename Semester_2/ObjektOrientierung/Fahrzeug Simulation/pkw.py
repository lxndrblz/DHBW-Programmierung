from kraftfahrzeug import Kraftfahrzeug
class pkw(Kraftfahrzeug):
    def __init__(self,fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht,hoechstgeschwindigkeit,leistung,anzahlSitzplaetze):
        super().__init__(fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht,hoechstgeschwindigkeit,leistung)
        self.anzahlSitzplaetze = anzahlSitzplaetze
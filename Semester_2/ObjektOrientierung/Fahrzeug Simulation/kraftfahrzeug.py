from fahrzeug import *
import datetime

class Kraftfahrzeug(Fahrzeug):
    def __init__(self,fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht,hoechstgeschwindigkeit,leistung):
        super().__init__(fahrzeugnummer,leergewicht,zulaessigesGesamtgewicht)
        self.leistung = leistung
        self.hoechstgeschwindigkeit = hoechstgeschwindigkeit
        now = datetime.datetime.now()

        datum = str(now.day) + "." + str(now.month) +"." + str(now.year + 2)

        self.tuev = datetime.datetime.strptime(datum, '%d.%m.%Y')


    def pruefeFahrerlaubnis(self):
        #TODO
        return True
    def pruefeTuev(self):
        now = datetime.datetime.now()
        return self.tuev > now

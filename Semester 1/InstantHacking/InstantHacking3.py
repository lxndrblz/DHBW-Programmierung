
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Eine Einfache Abfrage innerhalb einer Schleife

while True:   
    temperatureSpam = input("Was ist die Temperatur des Fleisches? ")
    if temperatureSpam < 50:
        print "Weiter kochen!"
    else:
        print "Bereit zum Essen!"
        break
def ganzZahl(nummer):
    ganzZahl = 0
    while ganzZahl <= nummer:
        ganzZahl =ganzZahl+1
    ganzZahl=ganzZahl -1
    return ganzZahl

nummer = input("Bitte eine Nummer eingeben: ")
#Manuell
print "Der ganzahlige Anteil ist: " + str(ganzZahl(nummer))
#System Funktion
print "Der ganzahlige Anteil ist (system): " + str(int(nummer))
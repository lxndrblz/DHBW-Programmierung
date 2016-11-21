#Schreiben Sie ein Programm, das "Bestanden" ausgibt, falls die Variable Punkte einen Wert größer gleich 50 hat
def bestehen(punkte):
    if (punkte >= 50):
        print("Bestanden")
    else:
        print("Nicht bestanden")
bestehen(45)

# Schreiben Sie ein Programm, das mit einer for-Schleife die folgende Ausgabe erzeugt:
# 0
# 2
# 4
# 6
# 8
# 10
# Ende !
def ausgabe():
    for i in range(0,11,2):
        print(i)
    print("Ende !")
ausgabe()
# Schreiben Sie ein Programm, das mit einer for-Schleife die folgende Ausgabe erzeugt:
# 10
# 8
# 6
# 4
# 2
# 0
# Ende !
def ausgabe():
    for i in range(10,-1,-2):
        print(i)
    print("Ende !")
ausgabe()

#Ergänzen Sie das folgende Programm, so dass die Vokale in s gezählt und ausgegeben werden. Gehen Sie dabei davon aus, dass s nur Kleinbuchstaben enthält.
s = "Hello world"
s.lower()
vokale = ['a','e','i','o','u']
AnzahlVokale = 0
for c in s:
    if (c in vokale):
        AnzahlVokale += 1
print(AnzahlVokale)

#Schreiben Sie ein Programm, das alle Zahlen > 0 bis zur Zahl "ende" aufsummiert und ausgibt:
ende = 10
summe = 0

while (ende >=0):
    summe=summe + ende
    ende -= 1
print(summe)

#Schreiben Sie ein Programm, das mit einer while-Schleife die folgende Ausgabe erzeugt:
index = 0
while index <= 10:
    print(index)
    index+=2
print("Ende !")



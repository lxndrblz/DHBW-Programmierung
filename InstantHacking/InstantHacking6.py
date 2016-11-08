#Euklid Methode

def euklid(a,b):
    while b != 0:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a
def setZaehler(a):
    global Zaehler
    Zaehler = 10

setZaehler(10)
print euklid(Zaehler,2)


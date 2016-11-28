#encoding=utf-8
#Erstellen Sie ein Programm, das einen String "rückwärts" ausgibt, also den letzten Buchstaben zuerst, dann den zweitletzten usw.
def backwards(s):
    for i in range(len(s)-1, -1, -1):
        print(s[i])
s = "Hello world"
print(backwards(s))
#Erweitern Sie das Programm so, dass geprüft wird, ob ein Wort ein Palindrom ist. Ein Palindrom ist ein Wort, das von vorne und von hinten gelesen gleich ist, z.B. "OTTO". Implementieren Sie dazu die Funktion is_palindrom(s), die True oder False zurücklifert, je nachdem, ob s ein Palindrom ist.
def is_palindrom(s):
    reverse = ''
    for i in range(len(s)-1, -1, -1):
        reverse = reverse + s[i]
    return reverse == s
print(is_palindrom("OttO"))
#Schreiben Sie ein Programm, das bestimmt, wie oft ein bestimmter String in einem anderen vorkommt, beispielsweise kommt "ei" 2x in "Kleingeist" vor.
def PatternInString(s, pattern):
    Anzahl = 0
    for i in range(0, len(s),2):
        if s[i:(i+2)] == pattern:
            Anzahl+=1
    return Anzahl

s = "Kleingeist"
pattern = "ei"
print(PatternInString(s, pattern))
# In dieser Aufgabe geht es darum, einen String (etwa einen Satz) in einzelne Wörter zu zerlegen. Gehen Sie davon aus, dass sich zwischen zwei Wörtern immer ein Leerzeichen befindet. Als Beispiel nehmen wir String s = „Das ist ein kurzer aber schöner Satz“;
# Schreiben Sie eine Funktion count_words(s), die die Anzahl der Wörter im übergebenen String zurückliefert (im Beispiel 7) und testen Sie diese.
# Erweitern Sie Ihr Programm so, dass die einzelnen Wörter jeweils in einer Zeile ausgegeben werden, im Beispiel also:
# Das
# ist
# ein
# kurzer
# aber
# schöner
# Satz
# Erstellen Sie dazu eine Funktion tokenize(s), die genau das tut.
# Hinweis: Das war vor einigen Jahren eine Klausuraufgabe, das ist in etwa der Schwierigkeitsgrad, den SIe in der Prüfung erwarten können.

#Ist Split funktion erlaubt?
def count_words(s):
    return len(s.split())
def tokenize(s):
    token = s.split()
    for t in token:
        print(t)
print(count_words("Das ist ein kurzer aber schöner Satz"))
tokenize("Das ist ein kurzer aber schöner Satz")

# Schreiben Sie eine Funktion encode(s), die einen String (der der Einfachheit halber nur aus Großbuchstaben besteht) mit RLE komprimiert.


def encode(s):
    previous = ''
    length = 0
    output = ''
    for c in s:
    
        if (c == previous or previous == ''):
            length += 1
        elif (c != previous):
            output = output + str(length) + previous
            length = 1
        previous = c
    #Ansonsten wird lezter Block ignoriert.
    return output + str(length) + previous

# Schreiben Sie eine Funktion decode(s), die einen RLE-komprimierten String wieder in die ursprüngliche Darstelluung umwandelt.def encode(s):


def decode(s):
    output = ''
    numberstr =  ''
    for c in s:
        if c.isdigit():
            numberstr = numberstr + c
        else:
            output += c * int(numberstr)
            numberstr = ''
    return output
print(encode("AAAAAAAAAABBBBBCCCCCCCCCCGXX"))
print(decode("5A5B10C4A5F1G"))


#Schreiben Sie ein Programm, das die ersten zehn Look And Say Zahlen berechnet
def say(s):
    
    output = ''
    count = 1
    last = ''
    if len(s) == 1:
        return '11'
    #Eins weiter zählen
    s += ' '
    for i in range(1, len(s)):
            #Zeichen gleich vorherigem?
            if s[i] != s[i-1]:
                output = output + str(count) + s[i-1]
                count = 1
            else:
                count += 1
    return output  

s = "1"
for i in range(10):
    s = say(s)
    print(s)

# Schreiben Sie eine Funktion read_term(term) , die einen als String übergebenen arithmetischen Ausdruck "vorliest",
# also aus 1*2/3-5 den String "eins mal zwei durch drei minus fünf" macht. Beschränken Sie sich zunächst auf
# einstellige Zahlen, also die von 0 bis 9. Erweitern Sie die Funktion so, dass auch Zahlen größer als 9 richtig
# umgewandelt werden.


def get_word(index):
    zahlen = ['','eins','zwei','drei','vier','fünf','sechs','sieben','acht','neun']
    return zahlen[index]


def get_operator(s):
    if s == "*":
        return " mal "
    elif s == "/":
        return " durch "
    elif s == "-":
        return " minus "
    elif s == "+":
        return " plus "


def read_term(term):
    output = ''
    for t in term:
        if t.isdigit():
            output += get_word(int(t))
        else:
            output += get_operator(t)
    return output
t = "1*2/3-5"
print(read_term(t))


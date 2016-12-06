#encoding=utf-8
'''
99 Bottles of Beer
'''

bottles = 99
while bottles > 1:
    print(str(bottles) + " bottles of beer on the wall," + str(bottles) + " bottles of beer. If one of those bottles should happen to fall")
    bottles -= 1
print("One (last) bottle of beer on the wall,")
print("One (last) bottle of beer.")
print("Take it down, pass it around,")
print("No (more) bottles of beer on the wall.")

'''
Check Palindrom
'''

p = "regallager"
def check_palindrom(s):
    return s == s[::-1]
print(check_palindrom(p))
# Sollte True ergeben

'''
Palindrom Wert
'''
p = "regallager"


def palindrom_wert(s):
    vokale = "aeiou"
    anzahl_konsonant = 0.0
    for c in s:
        if c not in vokale:
            anzahl_konsonant += 1
    return float(anzahl_konsonant / len(s))

print(palindrom_wert(p))
# Sollte 0.6 ergeben


'''
Check palindrom Satz
'''

p = "sei fein, nie fies"


def check_palindrom_satz(s):
    #Alle Satzzeichen entfernen
    pattern = "!@#$%^&*()[]{};:,./<>?\|`~-=_+ "
    for c in pattern:
        s = s.replace(c, "")
    return bool(s == s[::-1])
print(check_palindrom_satz(p))
# Sollte True sein
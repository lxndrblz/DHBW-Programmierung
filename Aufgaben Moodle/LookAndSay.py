# coding=utf-8
def lookandsay(s):
    # Output
    look = ''
    count = 1
    # Letztes Zeichen
    val = s[0]
    for c in s[1:]:
        # Zeichen ungleich vorherigem
        if (c != val):
            look = look + str(count) + val
            count = 1
            val = c
        else:
            count += 1
    look = look + str(count) + val
    return look


# Gibt nächste Zeile der Look and Say Zahlen aus
def look_one(s):
    return lookandsay(s)


# Liefert die nte Anzahl zurück
def look_n(s, n):
    ausgabe = s
    for i in range(n):
        ausgabe = lookandsay(ausgabe)
    return ausgabe


print(look_one('11'))
print(look_n('1', 3))

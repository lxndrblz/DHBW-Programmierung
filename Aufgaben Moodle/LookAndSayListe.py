# coding=utf-8
def lookandsay(l):
    # Output
    look = []
    count = 1
    # Letztes Zeichen
    val = l[0]
    for c in l[1:]:
        # Zeichen ungleich vorherigem
        if (c != val):
            look.append(count)
            look.append(val)
            count = 1
            val = c
        else:
            count += 1
    look.append(count)
    look.append(val)
    return look


# Gibt nächste Zeile der Look and Say Zahlen aus
def look_one(l):
    return lookandsay(l)


# Liefert die nte Anzahl zurück
def look_n(l, n):
    ausgabe = l
    for i in range(n):
        ausgabe=lookandsay(ausgabe)
    return ausgabe


print(look_one([1,1]))
print(look_n([1], 10))

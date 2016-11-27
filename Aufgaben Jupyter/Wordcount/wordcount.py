# coding=utf-8

# Um den folgenden Code einfacher zu halten, zerlegen wir den Text in einzelne Wörter und speichern die in einer
# Liste ab.


f = open("./testdata/short.txt")
words = []
for line in f:
    # Einzelne Wörter pro Zeile extrahieren
    wordsline = line.rstrip().split()
    for word in wordsline:
        words.append(word)

if len(words) != 67:
    print('Fehler !')

print(words)

# Um den Programmcode wieder verwenden zu können, definieren wir uns eine Funktion read_words(name), die eine Liste
# mit den Wörtern aus der Datei zurück liefert und eine Funktion count_words(words), die die Häufigkeit der Wörter in
#  der Liste list als Dictionary zurück liefert.
def read_words(name):
    f = open(name)
    words = []
    for line in f:
        # Einzelne Wörter pro Zeile extrahieren
        wordsline = line.rstrip().split()
        for word in wordsline:
            # Zur Wortliste hinzufügen
            words.append(word)
    return words


# Funktion zählt wie of ein Wort in einem Text vorkommt
def count_words(words):
    # Dictionary für Zuordnung Word und Anzahl
    counts = {}

    for word in words:
        # Existiert Dictionary Key bereits?
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

#Gibt das Wort mit dem höchsten Zählerwert zurück
def most_frequent_word(wordcount):
    # Index Häufigste Wort
    return max(wordcount, key=wordcount.get)

# Alle Wörter einlesen
words = read_words("./testdata/long.txt")
# Vorkommen der Wörter zählen
wordcount = count_words(words)
# Ausgabe Häufigstes Wort
mostfrequentword = most_frequent_word(wordcount)
print("Häufigstes Wort: " + mostfrequentword + " Anzahl: " + str(wordcount[mostfrequentword]))

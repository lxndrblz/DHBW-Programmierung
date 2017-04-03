#encoding=utf-8
Matrikelnummer = "9001624"

'''
Antwort: Formale Handlungsforschrift zur Lösung eines Problems in endlich vielen Schritten.
Die Programmiersprache ist die Beschreibung mit der

'''
'''
Antwort: Die ideale Größe einer Funktion hängt vom Umfang der Aufgabe ab. Gemäß dem Python Zen sollte eine
Funktion so kurz wie möglich sein, aber trotzdem noch lesbar sein. Manchmal ist es auch notwendig die eine Funktion
in weitere kleinere Unterfunktionen zu unterteilen, falls der Umfang zu groß wird.

'''

'''
Schreiben Sie ein Programm, das zu einer Zahl den entsprechenden Monat ausgibt, die Ausgabe zur Zahl 3 wäre also etwa "März". Schreiben Sie Ihr Programm so, dass es für alle zwölf Monate korrekt funktioniert.
'''

import locale
import calendar
locale.setlocale(locale.LC_ALL, 'de_DE')
print(calendar.month_name[4])



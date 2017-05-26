# DHBW-Programmierung
**Hinweis**

Dies sind **keine** offiziellen Lösungen aus dem Kurs _Programmierung_ an der DHBW.  Alle hier gezeigten Lösungen sind selbst erarbeitet und sollen als Inspiration für die Lösung einfacher Problemstellungen in Python dienen. 

Dieses Repository enthält alle Programmierübungen aus dem 1.  und 2. Semester Programmieren in Python an der DHBW Heidenheim. Ein Teil der Lösungen —wie die zu den Aufgabenstellungen aus dem Moodle LMS— sind noch Python 2.(x),  diese können aber auch relativ leicht auf Python 3.(x) angepasst werden.

Alle Lösungen für die Jupyter Umgebung und Objektorientierung sind in Python 3.(x) realisiert.

## Struktur dieses Repositories
```
├── Semester_1
│   ├── Aufgaben\ Jupyter
│   │   ├── Basic\ Functions
│   │   ├── Loops
│   │   ├── Strings
│   │   └── Wordcount
│   │       └── testdata
│   ├── Aufgaben\ Moodle
│   ├── InstantHacking
│   ├── Python\ Turtle
│   ├── Titanic
│   │   └── data
│   └── ToDo\ Anwendung
│       └── data
└── Semester_2
    ├── ObjektOrientierung
    │   ├── Bruchrechnen
    │   ├── Simulation
    │   └── ToDo\ Anwendung
    │       └── data
    ├── ToDo\ Anwendung
    │       └── data
    ├── ToDo\ Web
    │   ├── data
    │   ├── docs
    │   │   └── img
    │   ├── static
    │   │   ├── css
    │   │   └── fonts
    │   ├── templates
    └── Webserver
        ├── static
        └── templates
```
## Anwendung Funktionen Jupyter
Um die Lösungen in Jupyter auszuführen muss zunächst die eigentliche Funktion ausgeführt werden. Funktionen können mittels Shift+Enter ausgeführt werden.
```
def maximum(a,b):
    if(a>b):
        return a
    else:
        return b
```


Anschließend kann die Funktion kann wie folgt aufgerufen werden:
`maximum(5,9)`

Es sollte folgende Ausgabe erscheinen:
`9` :tada:
 
## Fehlende Imports beheben
Manche Lösungen nutzen Funktionen und Module, die nicht Teil der Standardinstallation sind. Alle hier verwendeten Module können mit pip nachinstalliert werden. Nachfolgender Befehl installiert das Modul _names_, das z.B. bei der [https://github.com/lxndrblz/DHBW-Programmierung/tree/master/Semester_2/ObjektOrientierung/Simulation](https://github.com/lxndrblz/DHBW-Programmierung/tree/master/Semester_2/ObjektOrientierung/Simulation) verwendet wird:

`pip3 install names`

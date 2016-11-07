#Ein Quadrat
go(60)
turn(90)
go(60)
turn(90)
go(60)
turn(90)
go(60)

#Ein Haus mit Dach
go(50)
turn(45)
go(35.35)
turn(90)
go(35.35)
turn(45)
go(50)
turn(90)
go(50)
turn(90)
go(50)
turn(90)
go(50)

#Sechseck zeichnen
for i in range(6):
	turn(60)
	go(60)

#Kreis zeichnen
segmente = 50
for i in range(segmente):
    turn(360/segmente)
	go(10)

#gestrichelte Linie Kreis
segmente = 50
for i in range(segmente):
    turn(360/segmente)
	go(10)
    if(i%2):
        pen_up()
    else:
        pen_down()
#Zeichnet eine Farn-Struktur
def farn(len):
    if(len > 2):
        go(len)
        turn(25)
        farn(len*0.5)
        turn(-35)
        farn(len * 0.7)
        turn(-25)
        farn(len*0.4)
        turn (35)
        go(-len)
    else:
        go(len)
        go(-len)

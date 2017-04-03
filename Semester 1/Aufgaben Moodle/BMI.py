# coding=utf-8

kategorie = [(0,16, "Spanferkel"),(16,17, "Hot Dog"),(17,18.5, "Lasagne"),(18.5, 25, "Hähnchen"),(25, 30, "Nudeln"),(30, 35, "Salami Brot"), (35, 40, "Käsebrot"), (40, 1000, "gar nichts")];
gewicht = raw_input("Bitte Gewicht eingeben (kg): ")
groesse = raw_input("Bitte Größe eingeben (m): ")
bmi = int(gewicht)/(float(groesse)**2)
# Kategorie finden
for k in kategorie:
    if k[0] <= bmi < k[1]:
        print(k[2])



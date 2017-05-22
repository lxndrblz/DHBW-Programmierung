from flask import Flask, request, render_template, url_for
app = Flask("TEST")
#Decorator defines route
@app.route("/")
def index():
    return render_template("rechner.html")

@app.route("/calc_bmi")
def calc_bmi():
    groesse = request.args.get('groesse')
    groesse = int(groesse)
    gewicht = request.args.get('gewicht')
    bmi = int(gewicht) / (float(groesse/100) ** 2)

    if(bmi < 19):
        img="sausage.jpg"
    elif(bmi>19 and bmi<25):
        img="nudeln.jpg"
    else:
        img="spinat.jpg"
    img = url_for('static', filename=img)
    return render_template("ergebnis.html", ergebnis=bmi, src=img)
if __name__ == '__main__':
    app.run(debug=True)

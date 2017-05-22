from flask import Flask, request, render_template
app = Flask("TEST")
#Decorator defines route
@app.route("/")
def index():
    return render_template("test.html")

@app.route("/calc_bmi")
def calc_bmi():
    groesse = request.args.get('groesse')
    groesse = int(groesse)
    gewicht = request.args.get('gewicht')
    bmi = int(gewicht) / (float(groesse/100) ** 2)
    img='/static/'
    if(bmi < 19):
        img+="sausage.jpg"
    elif(bmi>19 and bmi<25):
        img+="nudeln.jpg"
    else:
        img+="spinat.jpg"
    return render_template("ergebnis.html", ergebnis=bmi, src=img)
if __name__ == '__main__':
    app.run(debug=True)

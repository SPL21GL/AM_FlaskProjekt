from flask import Flask, redirect, request
from flask.templating import render_template
from models.models import db, Automarke, Kunden, Mietwagen
from forms.addAutoForm import AddAutoForm
from forms.addAutoForm import AddKundenForm
from forms.addAutoForm import AddMietwagen
from forms.EditKundenForm import editKundenForm

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key ="VerySecretSecretKeey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/autoapp"

csrf = CSRFProtect(app)
db.init_app(app)

#app.register_blueprint(Kunden_blueprint)

@app.route("/Kunden.html", methods = ["get", "post"])
def Kunden_requests():
    AddKundenFormObject = AddKundenForm()
    Kunde1 = db.session.query(Kunden).all()


    return render_template("Kunden.html", \
        headline="Automarke", \
        form2 = AddKundenFormObject, \
        items2 = Kunde1)

@app.route("/Auto.html", methods = ["get", "post"])
def Auto_request():

    addAutoFormObject = AddAutoForm()
    Auto1 = db.session.query(Automarke).all()


    return render_template("Auto.html", \
        headline="Automarke", \
        form1 = addAutoFormObject, \
        items1 = Auto1)


@app.route("/Miete.html", methods = ["get", "post"])
def Miete_request():

    Mietwagen1 = db.session.query(Mietwagen).all()
    AddMietwagenFormObject = AddMietwagen()
    
    return render_template("Miete.html", \
        headline="Automarke", \
        form3 = AddMietwagenFormObject, \
        items3 = Mietwagen1)


@app.route("/", methods = ["get", "post"])
def index():

    addAutoFormObject = AddAutoForm()
    AddKundenFormObject = AddKundenForm()
    AddMietwagenFormObject = AddMietwagen()
    

    if addAutoFormObject.validate_on_submit():
        #post kam zurück und ist valide
        print(addAutoFormObject.JaehrlicherUmsatz.data)
        print(addAutoFormObject.Gruendungsdatum.data)
        print(addAutoFormObject.MarkenName.data)
        print(addAutoFormObject.VerkaufszahlenProJahr.data)
        print(addAutoFormObject.Herststellland.data)

        #hier in DB Speichern
        newItem = Automarke()
        newItem.JaehrlicherUmsatz = addAutoFormObject.JaehrlicherUmsatz.data
        newItem.Gruendungsdatum = addAutoFormObject.Gruendungsdatum.data
        newItem.MarkenName = addAutoFormObject.CarMarkenNameName.data
        newItem.VerkaufszahlenProJahr = addAutoFormObject.VerkaufszahlenProJahr.data
        newItem.Herststellland = addAutoFormObject.Herststellland.data

        db.session.add(newItem)
        db.session.commit()
        return redirect("/")


    elif AddKundenFormObject.validate_on_submit():
        print(AddKundenFormObject.Vorname.data)
        print(AddKundenFormObject.Nachname.data)
        print(AddKundenFormObject.Geburtstag.data)
        print(AddKundenFormObject.Wohnohrt.data)
        print(AddKundenFormObject.Fuehrerscheinklasse.data)

        #hier in DB Speichern
        newKunden = Kunden()
        newKunden.Vorname = AddKundenFormObject.Vorname.data
        newKunden.Nachname = AddKundenFormObject.Nachname.data
        newKunden.Geburtstag = AddKundenFormObject.Geburtstag.data
        newKunden.Wohnohrt = AddKundenFormObject.Wohnohrt.data
        newKunden.Fuehrerscheinklasse = AddKundenFormObject.Fuehrerscheinklasse.data

        db.session.add(newKunden)
        db.session.commit()
        return redirect("/")

    elif AddMietwagenFormObject.validate_on_submit():
        print(AddMietwagenFormObject.Farbe.data)
        print(AddMietwagenFormObject.kmStand.data)
        print(AddMietwagenFormObject.Leistung.data)
        print(AddMietwagenFormObject.Erstzulasung.data)
        print(AddMietwagenFormObject.Kennzeichen.data)
        print(AddMietwagenFormObject.Baujahr.data)

        newMietwagen = Mietwagen()
        newMietwagen.Farbe = AddMietwagenFormObject.Farbe.data
        newMietwagen.kmStand = AddMietwagenFormObject.kmStand.data
        newMietwagen.Leistung = AddMietwagenFormObject.Leistung.data
        newMietwagen.Erstzulasung = AddMietwagenFormObject.Erstzulasung.data
        newMietwagen.Kennzeichen = AddMietwagenFormObject.Kennzeichen.data
        newMietwagen.Baujahr = AddMietwagenFormObject.Baujahr.data

        db.session.add(newMietwagen)
        db.session.commit()
        return redirect("/")
        
    Auto1 = db.session.query(Automarke).all()
    Kunde1 = db.session.query(Kunden).all()
    Mietwagen1 = db.session.query(Mietwagen).all()


    return render_template("base.html", \
        headline="Automarke", \
        form1 = addAutoFormObject, \
        form2 = AddKundenFormObject, \
        form3 = AddMietwagenFormObject, \
        items1 = Auto1, \
        items2 = Kunde1, \
        items3 = Mietwagen1)

def submitEditForm():
    editKundenFormObject = editKundenForm()

    if editKundenFormObject.validate_on_submit():
        
        KundenID = editKundenFormObject.Kunden.data
        Kunden_to_edit = db.session.query(Kunden).filter(Kunden.KundenID == KundenID).first()
        Kunden_to_edit.Vorname = editKundenFormObject.Vorname.data
        
        db.session.commit()

        return redirect("/")

    else:
        raise ("Fatal Error")

@app.route("/editKundenForm.py")
def showEditForm():
    KundenID = request.args["KundenID"]
    print(KundenID)
    
    Kunden_to_edit = db.session.query(Kunden).filter(Kunden.KundenID == KundenID).first()
    editKundenFormObject = editKundenForm()

    editKundenFormObject.KundenID.data =  Kunden_to_edit.KundenID
    editKundenFormObject.Vorname.data = Kunden_to_edit.Vorname
    editKundenFormObject.Nachname.data = Kunden_to_edit.Nachname
    editKundenFormObject.Geburtstag.data = Kunden_to_edit.Geburtstag
    editKundenFormObject.Wohnohrt.data = Kunden_to_edit.Wohnohrt
    editKundenFormObject.Fuehrerscheinklasse.data= Kunden_to_edit.Fuehrerscheinklasse
    


    return render_template("Kunden.html", form2 = editKundenForm)

app.run(debug=True)

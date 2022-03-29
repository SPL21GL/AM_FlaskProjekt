from flask import Flask, redirect, session
from flask.templating import render_template
from models.models import db, Automarke
from addAutoForm import AddAutoForm

app = Flask(__name__)
app.secret_key ="VerySecretSecretKeey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/autoapp"
db.init_app(app)

@app.route("/", methods = ["get", "post"])
def index():

    reload_count = session.get("number_of_reloads", 1)

    reload_count += 1

    session.update({"number_of_reloads": reload_count})


    addAutoFormObject = AddAutoForm()
    
    if addAutoFormObject.validate_on_submit():
        #post kam zurück und ist valide
       # print(addAutoFormObject.JaehrlicherUmsatz.data)
        #print(addAutoFormObject.Gruendungsdatum.data)
        #print(addAutoFormObject.MarkenName.data)
        #print(addAutoFormObject.VerkaufszahlenProJahr.data)
        #print(addAutoFormObject.Herststellland.data)



        #hier in DB Speichern
        
        #newItem = Automarke()
        #newItem.JaehrlicherUmsatz = addAutoFormObject.JaehrlicherUmsatz.data
        #newItem.Gruendungsdatum = addAutoFormObject.Gruendungsdatum.data
        #newItem.MarkenName = addAutoFormObject.CarMarkenNameName.data
        #newItem.VerkaufszahlenProJahr = addAutoFormObject.VerkaufszahlenProJahr.data
        #newItem.Herststellland = addAutoFormObject.Herststellland.data

        #db.session.add(newItem)
        db.session.commit()

        return redirect("/")

    
    items = db.session.query(Automarke).all()

    return render_template("index.html", \
        headline="Automarke", \
        form = addAutoFormObject, \
        items = items, \
        reload_count = reload_count)
    

app.run(debug=True)

from flask import Flask, redirect
from flask.templating import render_template
from flask import Blueprint
from models.models import Automarke, db

from forms.addAutoForm import AddAutoForm

Auto_blueprint = Blueprint('auto_blueprint', __name__)

@Auto_blueprint.route("/Auto.html", methods = ["get", "post"])
def Auto_request():

    addAutoFormObject = AddAutoForm()
    auto = db.session.query(Automarke).all()
    

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
        
    return render_template("Auto.html", \
        headline="Automarke", \
        form = addAutoFormObject, \
        auto = auto)

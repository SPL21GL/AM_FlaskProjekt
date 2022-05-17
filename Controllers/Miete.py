from flask.templating import render_template
from flask import Blueprint
from models.models import Mietwagen, db

from forms.addAutoForm import AddMietwagen

Miete_blueprint = Blueprint('miete_blueprint', __name__)


@Miete_blueprint.route("/Miete.html", methods=["get", "post"])
def Miete_request():

    mietwagen = db.session.query(Mietwagen).all()
    AddMietwagenFormObject = AddMietwagen()

    if AddMietwagenFormObject.validate_on_submit():
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

    return render_template("Miete.html",
                           headline="Automarke",
                           form=AddMietwagenFormObject,
                           mietwagen=mietwagen)

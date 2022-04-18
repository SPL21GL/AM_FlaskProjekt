""""
#from pickle import GET
from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import flask_sqlalchemy
from models.models import db, Kunden
from addAutoForm import AddKundenForm


Kunden_blueprint = Blueprint('kunden_blueprint', __name__)

@Kunden_blueprint.route("/Kunden")
def Kunden():
    # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    Kunden = session.query(Kunden).all()

    return render_template("base.html")

@Kunden_blueprint.route("/Kunden", methods=["GET", "POST"])
def Kunden_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    addKundenFormObject = AddKundenForm()
    if request.method =='POST':


        if addKundenFormObject.validate_on_submit():
            print(addKundenFormObject.Vorname.data)
            print(addKundenFormObject.Nachname.data)
            print(addKundenFormObject.Geburtstag.data)
            print(addKundenFormObject.Wohnohrt.data)
            print(addKundenFormObject.Fuehrerscheinklasse.data)

            newKundenItem = Kunden()
            newKundenItem.Vorname = addKundenFormObject.Vorname.data
            newKundenItem.Nachname = addKundenFormObject.Nachname.data
            newKundenItem.Geburtstag = addKundenFormObject.Geburtstag.data
            newKundenItem.Wohnohrt = addKundenFormObject.Wohnohrt.data
            newKundenItem.Fuehrerscheinklasse = addKundenFormObject.Fuehrerscheinklasse.data

            db.session.add(newKundenItem)
            db.session.commit()


            return redirect("/Kunden")
    
        else:
            return "Es geht nicht"

    else:
        return "Es geht nicht mal 2"

"""


    


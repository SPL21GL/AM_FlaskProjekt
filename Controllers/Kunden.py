from flask import flash, redirect, request
from flask.templating import render_template
from flask import Blueprint
from forms.EditKundenForm import editKundenForm
from forms.DeleteKundenForm import DeleteKunden
from forms.addKundenForm import AddKundenForm
from models.models import db, Kunden


Kunden_blueprint = Blueprint('kunden_blueprint', __name__)


@Kunden_blueprint.route("/Kunden.html", methods=["get", "post"])
def Kunden_requests():
    AddKundenFormObject = AddKundenForm()
    kunden = db.session.query(Kunden).all()

    if AddKundenFormObject.validate_on_submit():
        print(AddKundenFormObject.Vorname.data)
        print(AddKundenFormObject.Nachname.data)
        print(AddKundenFormObject.Geburtstag.data)
        print(AddKundenFormObject.Wohnohrt.data)
        print(AddKundenFormObject.Fuehrerscheinklasse.data)

        newKunden = Kunden()
        newKunden.Vorname = AddKundenFormObject.Vorname.data
        newKunden.Nachname = AddKundenFormObject.Nachname.data
        newKunden.Geburtstag = AddKundenFormObject.Geburtstag.data
        newKunden.Wohnohrt = AddKundenFormObject.Wohnohrt.data
        newKunden.Fuehrerscheinklasse = AddKundenFormObject.Fuehrerscheinklasse.data

        db.session.add(newKunden)
        db.session.commit()

        return redirect("/Kunden.html")

    return render_template("Kunden.html",
                           form=AddKundenFormObject,
                           kunden=kunden)


@Kunden_blueprint.route("/kunden/delete", methods=["post"])
def loescheKunde():
    delete_Kunden_form_obj = DeleteKunden()
    if delete_Kunden_form_obj.validate_on_submit():

        KundenIDToDelete = delete_Kunden_form_obj.KundenID.data
        KundenToDelete = db.session.query(Kunden).filter(
            Kunden.KundenID == KundenIDToDelete)
        KundenToDelete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Kunde mit der Id {KundenIDToDelete} wurde gelöscht")

    return redirect("/Kunden.html")


@Kunden_blueprint.route("/editForm", methods=["GET", "POST"])
def Kunden_edit():
    editKundenFormObject = editKundenForm()

    Kunden_to_edit = db.session.query(Kunden).filter(
        Kunden.KundenID == editKundenFormObject.KundenID.data).first()

    if request.method == "POST":
        if editKundenFormObject.validate_on_submit():

            Kunden_to_edit = db.session.query(Kunden).filter(
                Kunden.KundenID == editKundenFormObject.KundenID.data).first()

            Kunden_to_edit.Vorname = editKundenFormObject.Vorname.data
            Kunden_to_edit.Nachname = editKundenFormObject.Nachname.data
            Kunden_to_edit.Geburtstag = editKundenFormObject.Geburtstag.data
            Kunden_to_edit.Wohnort = editKundenFormObject.Wohnohrt.data
            Kunden_to_edit.Fuehrerscheinklasse = editKundenFormObject.Fuehrerscheinklasse.data

            db.session.commit()

            return redirect("/Kunden.html")

    else:
        kundenID = request.args["KundenID"]

        Kunden_to_edit = db.session.query(Kunden).filter(
            Kunden.KundenID == kundenID).first()

        editKundenFormObject.KundenID.data = Kunden_to_edit.KundenID
        editKundenFormObject.Vorname.data = Kunden_to_edit.Vorname
        editKundenFormObject.Nachname.data = Kunden_to_edit.Nachname
        editKundenFormObject.Geburtstag.data = Kunden_to_edit.Geburtstag
        editKundenFormObject.Wohnohrt.data = Kunden_to_edit.Wohnort
        editKundenFormObject.Fuehrerscheinklasse.data = Kunden_to_edit.Fuehrerscheinklasse

        return render_template("EditKundenForm.html", form=editKundenFormObject)

    return render_template("EditKundenForm.html", form=editKundenFormObject)

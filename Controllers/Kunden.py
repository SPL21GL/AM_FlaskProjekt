from flask import flash, redirect
from flask.templating import render_template
from flask import Blueprint
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


"""
def submitEditForm():
    editKundenFormObject = editKundenForm()

    if editKundenFormObject.validate_on_submit():
        KundenID = editKundenFormObject.Kunden.data
        Kunden_to_edit = db.session.query(Kunden).filter(
            Kunden.KundenID == KundenID).first()
        Kunden_to_edit.Vorname = editKundenFormObject.Vorname.data
        db.session.commit()

        return redirect("/")

    else:
        raise ("Fatal Error")


@Kunden_blueprint.route("/editKundenForm.py")
def showEditForm():
    KundenID = request.args["KundenID"]
    print(KundenID)

    Kunden_to_edit = db.session.query(Kunden).filter(
        Kunden.KundenID == KundenID).first()
    editKundenFormObject = editKundenForm()

    editKundenFormObject.KundenID.data = Kunden_to_edit.KundenID
    editKundenFormObject.Vorname.data = Kunden_to_edit.Vorname
    editKundenFormObject.Nachname.data = Kunden_to_edit.Nachname
    editKundenFormObject.Geburtstag.data = Kunden_to_edit.Geburtstag
    editKundenFormObject.Wohnohrt.data = Kunden_to_edit.Wohnohrt
    editKundenFormObject.Fuehrerscheinklasse.data = Kunden_to_edit.Fuehrerscheinklasse

    return render_template("Kunden.html", form=editKundenForm)

"""

from flask.templating import render_template
from flask import Blueprint, flash, redirect, request
from forms.EditMietwagenForm import editMietwagen
from models.models import Mietwagen, db
from forms.DeleteMietwagenForm import DeleteMietwagen

from forms.addMietenForm import AddMietwagen

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

        return redirect("/Miete.html")

    return render_template("Miete.html",
                           form=AddMietwagenFormObject,
                           mietwagen=mietwagen)


@Miete_blueprint.route("/Mietwagen/delete", methods=["post"])
def loescheMietwagen():
    delete_Mietwagen_form_obj = DeleteMietwagen()
    if delete_Mietwagen_form_obj.validate_on_submit():

        AutoIDToDelete = delete_Mietwagen_form_obj.AutoID.data
        AutoToDelete = db.session.query(Mietwagen).filter(
            Mietwagen.AutoID == AutoIDToDelete)
        AutoToDelete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Kunde mit der Id {AutoIDToDelete} wurde gelöscht")

    return redirect("/Miete.html")


@Miete_blueprint.route("/editFormMiete", methods=["GET", "POST"])
def Mietwagen_edit():
    editMietwagenFormObject = editMietwagen()

    Mietwagen_to_edit = db.session.query(Mietwagen).filter(
        Mietwagen.AutoID == editMietwagenFormObject.AutoID.data).first()

    if request.method == "POST":
        if editMietwagenFormObject.validate_on_submit():

            Mietwagen_to_edit = db.session.query(Mietwagen).filter(
                Mietwagen.AutoID == editMietwagenFormObject.AutoID.data).first()

            print(Mietwagen_to_edit)

            Mietwagen_to_edit.Farbe = editMietwagenFormObject.Farbe.data
            Mietwagen_to_edit.kmStand = editMietwagenFormObject.kmStand.data
            Mietwagen_to_edit.Leistung = editMietwagenFormObject.Leistung.data
            Mietwagen_to_edit.Erstzulasung = editMietwagenFormObject.Erstzulasung.data
            Mietwagen_to_edit.Kennzeichen = editMietwagenFormObject.Kennzeichen.data
            Mietwagen_to_edit.Baujahr = editMietwagenFormObject.Baujahr.data

            db.session.commit()

            return redirect("/Miete.html")

    else:
        mietwagenID = request.args["AutoID"]

        Mietwagen_to_edit = db.session.query(Mietwagen).filter(
            Mietwagen.AutoID == mietwagenID).first()

        editMietwagenFormObject.AutoID.data = Mietwagen_to_edit.AutoID
        editMietwagenFormObject.Farbe.data = Mietwagen_to_edit.Farbe
        editMietwagenFormObject.kmStand.data = Mietwagen_to_edit.kmStand
        editMietwagenFormObject.Leistung.data = Mietwagen_to_edit.Leistung
        editMietwagenFormObject.Erstzulasung.data = Mietwagen_to_edit.Erstzulasung
        editMietwagenFormObject.Kennzeichen.data = Mietwagen_to_edit.Kennzeichen
        editMietwagenFormObject.Baujahr.data = Mietwagen_to_edit.Baujahr

        return render_template("EditMietwagenForm.html", form=editMietwagenFormObject)

    return render_template("EditMietwagenForm.html", form=editMietwagenFormObject)

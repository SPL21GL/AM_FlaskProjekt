from flask.templating import render_template
from flask import Blueprint, flash, redirect, request
from forms.EditAutoForm import editAutoForm
from forms.DeleteAutoForm import DeleteAuto
from forms.addAutoForm import AddAutoForm
from models.models import Automarke, db

Auto_blueprint = Blueprint('auto_blueprint', __name__)


@Auto_blueprint.route("/Auto.html", methods=["get", "post"])
def Auto_request():

    auto = db.session.query(Automarke).all()
    addAutoFormObject = AddAutoForm()

    if addAutoFormObject.validate_on_submit():
        print(addAutoFormObject.JaehrlicherUmsatz.data)
        print(addAutoFormObject.Gruendungsjahr.data)
        print(addAutoFormObject.MarkenName.data)
        print(addAutoFormObject.VerkaufszahlenProJahr.data)
        print(addAutoFormObject.Herststellland.data)

        newAuto = Automarke()
        newAuto.JaehrlicherUmsatz = addAutoFormObject.JaehrlicherUmsatz.data
        newAuto.Gruendungsjahr = addAutoFormObject.Gruendungsjahr.data
        newAuto.MarkenName = addAutoFormObject.MarkenName.data
        newAuto.VerkaufszahlenProJahr = addAutoFormObject.VerkaufszahlenProJahr.data
        newAuto.Herststellland = addAutoFormObject.Herststellland.data

        db.session.add(newAuto)
        db.session.commit()

        return redirect("/Auto.html")

    return render_template("Auto.html",
                           form=addAutoFormObject,
                           auto=auto)


@Auto_blueprint.route("/auto/delete", methods=["post"])
def loescheKunde():
    delete_Auto_form_obj = DeleteAuto()
    if delete_Auto_form_obj.validate_on_submit():

        MarkenIDToDelete = delete_Auto_form_obj.MarkenID.data
        MarkenToDelete = db.session.query(Automarke).filter(
            Automarke.MarkenID == MarkenIDToDelete)
        MarkenToDelete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Automarke mit der Id {MarkenIDToDelete} wurde gelöscht")

    return redirect("/Auto.html")


@Auto_blueprint.route("/editFormAuto", methods=["GET", "POST"])
def Auto_edit():
    editAutoFormObject = editAutoForm()

    Auto_to_edit = db.session.query(Automarke).filter(
        Automarke.MarkenID == editAutoFormObject.MarkenID.data).first()

    if request.method == "POST":
        if editAutoFormObject.validate_on_submit():

            Auto_to_edit = db.session.query(Automarke).filter(
                Automarke.MarkenID == editAutoFormObject.MarkenID.data).first()

            Auto_to_edit.JaehrlicherUmsatz = editAutoFormObject.JaehrlicherUmsatz.data
            Auto_to_edit.Gruendungsjahr = editAutoFormObject.Gruendungsjahr.data
            Auto_to_edit.MarkenName = editAutoFormObject.MarkenName.data
            Auto_to_edit.VerkaufszahlenProJahr = editAutoFormObject.VerkaufszahlenProJahr.data
            Auto_to_edit.Herststellland = editAutoFormObject.Herststellland.data

            db.session.commit()

            return redirect("/Auto.html")

    else:
        markenID = request.args["MarkenID"]

        Auto_to_edit = db.session.query(Automarke).filter(
            Automarke.MarkenID == markenID).first()

        editAutoFormObject.MarkenID.data = Auto_to_edit.MarkenID
        editAutoFormObject.JaehrlicherUmsatz.data = Auto_to_edit.JaehrlicherUmsatz
        editAutoFormObject.Gruendungsjahr.data = Auto_to_edit.Gruendungsjahr
        editAutoFormObject.MarkenName.data = Auto_to_edit.MarkenName
        editAutoFormObject.VerkaufszahlenProJahr.data = Auto_to_edit.VerkaufszahlenProJahr
        editAutoFormObject.Herststellland.data = Auto_to_edit.Herststellland

        return render_template("EditAutoForm.html", form=editAutoFormObject)

    return render_template("EditAutoForm.html", form=editAutoFormObject)

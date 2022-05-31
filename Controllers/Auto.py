from flask.templating import render_template
from flask import Blueprint, flash, redirect
from forms.addAutoForm import AddAutoForm
from forms.DeleteAutoForm import DeleteAuto
from models.models import Automarke, db

Auto_blueprint = Blueprint('auto_blueprint', __name__)


@Auto_blueprint.route("/Auto.html", methods=["get", "post"])
def Auto_request():

    addAutoFormObject = AddAutoForm()
    auto = db.session.query(Automarke).all()

    if addAutoFormObject.validate_on_submit():
        print(addAutoFormObject.JaehrlicherUmsatz.data)
        print(addAutoFormObject.Gruendungsdatum.data)
        print(addAutoFormObject.MarkenName.data)
        print(addAutoFormObject.VerkaufszahlenProJahr.data)
        print(addAutoFormObject.Herststellland.data)

        # hier in DB Speichern
        newAuto = Automarke()
        newAuto.JaehrlicherUmsatz = addAutoFormObject.JaehrlicherUmsatz.data
        newAuto.Gruendungsdatum = addAutoFormObject.Gruendungsdatum.data
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

    flash(f"Kunde mit der Id {MarkenIDToDelete} wurde gelöscht")

    return redirect("/Auto.html")

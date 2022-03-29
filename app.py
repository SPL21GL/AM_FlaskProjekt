from flask import Flask, render_template, session, redirect
from model import Automarke, db
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
        print(addAutoFormObject.FirstName.data)
        print(addAutoFormObject.LastName.data)
        print(addAutoFormObject.CarName.data)
        print(addAutoFormObject.description.data)
        print(addAutoFormObject.dueDate.data)
        print(addAutoFormObject.isDone.data)
        #hier in DB Speichern
        
        newItem = Automarke()
        newItem.FirstName = addAutoFormObject.FirstName.data
        newItem.LastName = addAutoFormObject.LastName.data
        newItem.CarName = addAutoFormObject.CarName.data
        newItem.description = addAutoFormObject.description.data
        newItem.dueDate = addAutoFormObject.dueDate.data
        newItem.isDone = addAutoFormObject.isDone.data

        db.session.add(newItem)
        db.session.commit()

        return redirect("/")

    
    items = db.session.query(Automarke).all()

    return render_template("index.html", \
        headline="Automarke", \
        form = addAutoFormObject, \
        items = items, \
        reload_count = reload_count)
    

app.run()

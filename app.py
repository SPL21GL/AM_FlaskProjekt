from flask import Flask
from Controllers.Kunden import Kunden_blueprint
from Controllers.Auto import Auto_blueprint
from Controllers.Miete import Miete_blueprint
from Controllers.index import index_blueprint
from models.models import db

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "VerySecretSecretKeey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/autoapp"

csrf = CSRFProtect(app)
db.init_app(app)

app.register_blueprint(Kunden_blueprint)
app.register_blueprint(Auto_blueprint)
app.register_blueprint(Miete_blueprint)
app.register_blueprint(index_blueprint)

app.run(debug=True)

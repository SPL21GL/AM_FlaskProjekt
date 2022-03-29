# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Automarke(db.Model):
    __tablename__ = 'automarke'

    MarkenID = db.Column(db.Integer, primary_key=True, unique=True)
    JaehrlicherUmsatz = db.Column(db.Numeric(10, 0))
    Gruendungsdatum = db.Column(db.Date)
    MarkenName = db.Column(db.String(128))
    VerkaufszahlenProJahr = db.Column(db.Numeric(10, 0), nullable=False)
    Herststellland = db.Column(db.String(128))



class Kunden(db.Model):
    __tablename__ = 'kunden'

    KundenID = db.Column(db.Integer, primary_key=True, unique=True)
    Vorname = db.Column(db.String(128))
    Nachname = db.Column(db.String(128))
    Geburtstag = db.Column(db.Date)
    Wohnort = db.Column(db.String(64))
    Fuehrerscheinklasse = db.Column(db.String(32))



class Mietwagen(db.Model):
    __tablename__ = 'mietwagen'

    AutoID = db.Column(db.Integer, primary_key=True, unique=True)
    Farbe = db.Column(db.String(32))
    kmStand = db.Column(db.Numeric(10, 0))
    Leistung = db.Column(db.Numeric(10, 0))
    Erstzulasung = db.Column(db.Date)
    Kennzeichen = db.Column(db.String(64))
    Baujahr = db.Column(db.Date)
    MarkenID = db.Column(db.ForeignKey('automarke.MarkenID'), index=True)

    automarke = db.relationship('Automarke', primaryjoin='Mietwagen.MarkenID == Automarke.MarkenID', backref='mietwagens')



class MietwagenKunden(db.Model):
    __tablename__ = 'mietwagen_kunden'

    Mietwagen_KundenID = db.Column(db.Integer, primary_key=True, unique=True)
    AutoID = db.Column(db.Integer)
    KundenID = db.Column(db.Integer)

create database if not exists Autoapp;
use Autoapp;

create table if not exists Automarke
(
MarkenID int auto_increment unique key primary key,
JaehrlicherUmsatz decimal,
Gruendungsdatum date,
MarkenName varchar(128),
VerkaufszahlenProJahr decimal not null,
Herststellland varchar (128)
);


create table if not exists Mietwagen
(
AutoID int auto_increment unique key primary key,
Farbe varchar (32),
kmStand decimal,
Leistung decimal,
Erstzulasung date,
Kennzeichen varchar(64),
Baujahr date,
MarkenID int
);

#alter table Mietwagen
#add constraint markenForeignKey foreign key (MarkenID) 
#references Automarke (MarkenID);


create table if not exists Kunden
(
KundenID int auto_increment unique key primary key,
Vorname varchar(128),
Nachname varchar(128),
Geburtstag date,
Wohnort varchar (64),
Fuehrerscheinklasse varchar(32)
);

create table if not exists Mietwagen_Kunden
(
Mietwagen_KundenID int auto_increment unique key primary key,
AutoID int,
KundenID int
);




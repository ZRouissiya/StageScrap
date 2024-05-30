from views import app_views
from models.scrapMAStage import MAStage
from flask import render_template,Flask,url_for,session,redirect,send_file
from threading import Thread
from time import sleep
import json


@app_views.route('/demandesMA',strict_slashes=False)
@app_views.route("/demandesMA/<numP>",strict_slashes=False)
def demandesMA(numP=2):
    if 'dataMA' in session:
        return render_template("demandesMA.html",demandes=session['dataMA'])
    scr=MAStage()
    demandes=scr.scrapData(numPage=numP)
    f=['Titre', 'Domaine', 'Duree', 'Niveau', 'Lien']
    session['dataMA']=demandes
    session['fieldsMA']=f
    return render_template("demandesMA.html",demandes=demandes)



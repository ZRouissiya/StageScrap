from views import app_views
from models.scrapStagiaires import scrap
from flask import Flask, render_template,url_for,session,redirect,send_file,jsonify
from threading import Thread
from time import sleep
import pandas as pd
import plotly.express as px


@app_views.route('/demandes',strict_slashes=False)
@app_views.route("/demandes/<numP>",strict_slashes=False)
def demandes(numP=2):
    if 'data'in session:
        return render_template("demandes.html",demandes=session['data'])
    scr=scrap()
    demandes=scr.demandes(numPage=numP)
    f= ['Date de debut', 'Niveau', 'Ecole', 'Secteur', 'Lieu','Lien']
    session['data']=demandes
    session['fields']=f
    return render_template("demandes.html",demandes=demandes)


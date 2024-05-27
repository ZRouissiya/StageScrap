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
    scr=scrap()
    demandes=scr.demandes(numPage=numP)
    f= ['Date de debut', 'Niveau', 'Ecole', 'Secteur', 'Lieu','Lien']
    session['data']=demandes
    session['fields']=f
    return render_template("demandes.html",demandes=demandes,numPage=numP)

@app_views.route('/graph-data')
def graph_data():
    data = {
        'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 25, 30, 35]
    }
    fig = px.line(pd.DataFrame(data), x='x', y='y', title='Sample Line Plot')
    return jsonify(fig.to_json())
from views import app_views
from flask import Flask,jsonify
from models.scrapStagiaires import scrap
from models.scrapMAStage import  MAStage


@app_views.route('/graph-data-demandes')
def graph_data_demandes():
    scr=scrap()
    demandes=scr.demandes(numPage=5)    
    return jsonify(demandes)
@app_views.route('/graph-data-demandesMA')
def graph_data_demandesMA():
    scr=MAStage()
    demandes=scr.scrapData(numPage=2)
    return jsonify(demandes)
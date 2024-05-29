from views import app_views
from flask import jsonify,session
from models.scrapStagiaires import scrap
from models.scrapMAStage import MAStage

@app_views.route('/latest-data',strict_slashes=False)
def latestData():
    data=[]
    scr=scrap()
    demandes=scr.demandes()
    session['demandes']=demandes
    data.append(demandes)
    scr=MAStage()
    demandesMA=scr.scrapData(numPage=2)
    session['demandesMA']=demandesMA
    data.append(demandesMA[12:])
    return jsonify(data)
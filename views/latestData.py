from views import app_views
from flask import jsonify
from models.scrapStagiaires import scrap
from models.scrapMAStage import MAStage
@app_views.route('/latest-data',strict_slashes=False)
def latestData():
    data=[]
    scr=scrap()
    demandes=scr.demandes()
    data.append(demandes)
    scr=MAStage()
    demandesMA=scr.scrapData(numPage=2)
    data.append(demandesMA[10:])
    return jsonify(data)
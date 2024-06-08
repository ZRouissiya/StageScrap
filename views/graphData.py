from views import app_views
from flask import jsonify,session
from collections import defaultdict
from models.scrapStagiaires import scrap
from models.scrapMAStage import  MAStage
from datetime import datetime

@app_views.route('/graph-data-demandes')
def graph_data_demandes():
    scr=scrap()
    demandes=scr.demandes(numPage=3)    
    return jsonify(demandes)

@app_views.route('/graph-data-demandesMA')
def graph_data_demandesMA():
    scr=MAStage()
    demandes=scr.scrapData(numPage=2)
    return jsonify(demandes)

@app_views.route('/graph-data-secteurs', methods=['GET'])
def graph_data_secteurs():
    secteurs_data = defaultdict(lambda: defaultdict(int))
    
    for entry in session['stagiaires']:
        secteur = entry['Secteur']
        date_de_debut = entry['Date de debut']
        formatted_date = datetime.strptime(date_de_debut, '%d/%m/%Y').strftime('%d/%m/%Y')
        secteurs_data[formatted_date][secteur] += 1

    secteurs_data = {date: dict(secteurs) for date, secteurs in secteurs_data.items()}

    response_data = {
        'dates': sorted(list(secteurs_data.keys())),
        'data': secteurs_data
    }

    return jsonify(response_data)

@app_views.route('/graph-data-niveau')
def fetch_data_for_chart():
    marocAnnonces = session.get('marocAnnonces', [])
    
    data = []
    for item in marocAnnonces:
        level = item.get('Niveau')
        if level:
            existing_item = next((x for x in data if x['level'] == level), None)
            if existing_item:
                existing_item['count'] += 1
            else:
                data.append({'level': level, 'count': 1})

    return jsonify(data)


@app_views.route('/graph-data-domaine')
def fetch_domaines_data():
    marocAnnonces = session.get('marocAnnonces', [])
    
    domaines = {}
    for entry in marocAnnonces:
        domaine = entry.get('Domaine')
        if domaine:
            if domaine in domaines:
                domaines[domaine] += 1
            else:
                domaines[domaine] = 1
    
    return jsonify({'domaines': list(domaines.keys()), 'counts': list(domaines.values())})
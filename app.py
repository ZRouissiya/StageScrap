from flask import Flask,render_template,session,jsonify
from views import app_views

app=Flask(__name__)
app.secret_key='key'
app.register_blueprint(app_views)



@app.route('/',strict_slashes=False)
def index():
    if 'logged' in session:
        if session['logged']:
            return render_template("index.html",logged=session['logged'])
        return render_template("index.html")
    return render_template("index.html")

@app.route('/test')
def test():
    return render_template('accounts/profileError.html',fullname=session['nom']+' '+session['prenom'],nom=session['nom'],prenom=session['prenom'],email=session['email'],lastLogin=session['lastLogin'],creationDate=session['creationDate'])

@app.route('/graph-data-secteurs', methods=['GET'])
def graph_data_secteurs():
    secteurs = {}
    for entry in session['stagiaires']:
        secteur = entry['Secteur']
        date_de_debut = entry['Date de debut']
        if secteur in secteurs:
            secteurs[secteur]['count'] += 1
            secteurs[secteur]['dates'].append(date_de_debut)
        else:
            secteurs[secteur] = {'count': 1, 'dates': [date_de_debut]}
    
    # Prepare the response data
    response_data = {
        'secteurs': list(secteurs.keys()),
        'counts': [secteurs[secteur]['count'] for secteur in secteurs],
        'dates': [secteurs[secteur]['dates'] for secteur in secteurs]
    }
    
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)

from flask import send_file,session
from models.csv import dCsv
from views import app_views

@app_views.route('/downloadCsv/<site>', methods=['GET'])
def download(site):
    try:
        csv= dCsv()
        file=csv.dataToCsv(fields=session['fields'],data=session[site])
        return send_file(file,as_attachment=True,download_name='file.csv' ,mimetype='text/csv')
    except Exception as e:
        return f"Erreur lors de la création du fichier CSV : {str(e)}", 500
    
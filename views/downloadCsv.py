from flask import Flask,request,render_template_string, send_file,session
from models.csv import dCsv
from views import app_views

@app_views.route('/downloadCsv', methods=['GET', 'POST'])
def download():
    f=session['fields']
    try:
        csv= dCsv()
        file=csv.dataToCsv(fields=f,data=session['data'])
        return send_file(file,as_attachment=True,download_name='file.csv' ,mimetype='text/csv')
    except Exception as e:
        return f"Erreur lors de la création du fichier CSV : {str(e)}", 500
    
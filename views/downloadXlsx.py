from views import app_views
from flask import send_file,redirect,request,session
from models.csv import dCsv
from models.xlsx import dXlsx

@app_views.route('/downloadXlsx',methods=['GET','POST'])
def downloadXlsx():
    f=session['fields']
    try:
        csv=dCsv()
        csvFile=csv.dataToCsv(fields=f,data=session['data'])
        xlsx=dXlsx()
        file=xlsx.csvToXlsx(file=csvFile)
        return send_file(file,as_attachment=True,download_name='file.xlsx' ,mimetype='application/vnd.ms-excel')
    except Exception as e:
        return f"Erreur lors de la création du fichier CSV : {str(e)}", 500
from views import app_views
from flask import send_file,session,abort
from models.csv import dCsv
from models.xlsx import dXlsx

@app_views.route('/downloadXlsx/<site>',methods=['GET'])
def downloadXlsx(site):
    try:
        csv=dCsv()
        csvFile=csv.dataToCsv(fields=session['fields'],data=session[site])
        xlsx=dXlsx()
        file=xlsx.csvToXlsx(file=csvFile) 
        return send_file(file,as_attachment=True,download_name='file.xlsx' ,mimetype='application/vnd.ms-excel')
    except Exception as e:
        return abort(500)
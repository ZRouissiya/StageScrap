from flask import Flask,make_response,jsonify,request,render_template,redirect,session,send_file,render_template_string,Response
from views import app_views
from models.scrapStagiaires import scrap
import mysql.connector
import csv
import io
import glob
from xlsxwriter.workbook import Workbook

app=Flask(__name__)
app.secret_key='key'
app.register_blueprint(app_views)



@app.route('/',strict_slashes=False)
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

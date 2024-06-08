from flask import render_template,session,redirect
from views import app_views
from models.scrapStagiaires import  scrap
from models.scrapMAStage import MAStage
@app_views.route("/dashboard",strict_slashes=False)
def dashboard():
    if session.get('logged'):
        scr=scrap()
        demandes=scr.demandes(numPage=3)
        session['stagiaires']=demandes
        scr=MAStage()
        demandes=scr.scrapData(numPage=2)
        session['marocAnnonces']=demandes
        return render_template("dashboard.html",email=session['email'],Stagiaires=session['stagiaires'],MarocAnnonces=session['marocAnnonces'])
    return redirect("/")
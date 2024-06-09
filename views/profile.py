from flask import render_template,session,redirect,abort
from views  import app_views
@app_views.route("/profile",strict_slashes=False)
def profile():
    if 'logged' in session:
        if session['logged']:
            return render_template("accounts/profile.html",fullname=session['nom']+' '+session['prenom'],nom=session['nom'],prenom=session['prenom'],email=session['email'],lastLogin=session['lastLogin'],creationDate=session['creationDate'])
        return redirect('/',code=303)
    return abort(401)

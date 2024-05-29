from flask import render_template,session,redirect
from views import app_views
@app_views.route("/dashboard",strict_slashes=False)
def dashboard():
    if session.get('logged'):
        return render_template("dashboard.html")
    return redirect("/")
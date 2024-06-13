from flask import Flask,render_template,session
from views import app_views


app=Flask(__name__)
app.secret_key='key'
app.register_blueprint(app_views)



@app.route('/',strict_slashes=False)
def index():
    if 'user' in session:
        return render_template("index.html",user=True)
    return render_template("index.html")

@app.errorhandler(404)
def error404(e):
    return render_template("errorPages/error404.html",logged=session.get('logged')),404

@app.errorhandler(401)
def error401(e):
    return render_template("errorPages/error401.html",logged=session.get('logged')),401

@app.errorhandler(500)
def error500(e):
    return render_template("errorPages/error500.html",logged=session.get('logged')),500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask,render_template,session
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



if __name__ == "__main__":
    app.run(debug=True)

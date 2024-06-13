from views import app_views
from flask import request,render_template,session,redirect,abort
import mysql.connector as con
from models.user import User
from flask_bcrypt import Bcrypt
import pickle
bc=Bcrypt()
db=con.connect(host="localhost",user="root",password="",database='db_stage')
cursor=db.cursor()

@app_views.route('/logIn',methods=['POST'],strict_slashes=False)
def logIn():
    email=request.form['email']
    try:
        cursor.execute(f"SELECT * FROM user WHERE email='{email}'")
        rs=cursor.fetchall()
        if len(rs) > 0:
            password=request.form['password']
            if bc.check_password_hash(rs[0][2],password):
                cursor.execute(f"SELECT * FROM userData WHERE userId='{rs[0][0]}'")
                rs_data=cursor.fetchall()
                creationDate=rs_data[0][3]
                lastLogin=rs_data[0][4]
                nom=rs_data[0][1]
                prenom=rs_data[0][2]
                currentUser=User(prenom,nom,email,password,creationDate,lastLogin,rs[0][0])
                session['user']=pickle.dumps(currentUser)
                return redirect("/dashboard",code=301)
    except Exception as e:
        return redirect("/",code=303)
    return redirect("/",code=303)

@app_views.route('/signUp', methods=['POST'],strict_slashes=False)
def signUp():
    
    nom=request.form.get('nom')
    prenom = request.form.get('prenom')
    email=request.form.get('email')
    password=request.form.get('password')
    conPassword=request.form.get('conPassword')
    if(password == conPassword):
        try:
            user=User(prenom,nom,email,password)
            if user.insert():
                session['user']=pickle.dumps(user)
                return redirect("/dashboard",code=301)
        except Exception as e:
            return redirect("/",code=302)
    return redirect("/",code=303)


@app_views.route('/logout',strict_slashes=False)
def logout():
    if 'user' in session:
        try:
            currentUser=session['user']
            user=pickle.loads(currentUser)
            if user.logOut():
                session.pop('user')
                return redirect('/',code=301)
        except Exception as e:
            return redirect('/dashboard',code=303)
        return redirect('/dashboard',code=303)
        
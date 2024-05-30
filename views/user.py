from views import app_views
from flask import request,render_template,session,redirect,jsonify,Response
import mysql.connector as con
from flask_bcrypt import Bcrypt
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
                    session['email']=email
                    session['password']=password
                    session['logged']=True
                    return redirect("/dashboard",code=301)
    except Exception as e:
        print(e)
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
            hashedPwd=bc.generate_password_hash(password).decode("utf-8")
            sql="INSERT INTO user (email,password) VALUES (%s,%s)"
            val=(email,hashedPwd)
            cursor.execute(sql,val)
            id=cursor.lastrowid
            sql2="INSERT INTO userData (userId,nom,prenom,creationDate,lastLogin) VALUES (%s,%s,%s,CURDATE(),CURDATE())"
            val2=(int(id),nom,prenom)
            cursor.execute(sql2,val2)
            db.commit()
            session['email']=email
            session['password']=password
            session['logged']=True
            return redirect("/dashboard",code=301)
        except Exception as e:
            print("erreur")
            return redirect("/",code=303)

        
    return redirect("/",code=303)

    

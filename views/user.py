from views import app_views
from flask import request,render_template,session,redirect
import mysql.connector as con
import datetime
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
                    cursor.execute(f"SELECT * FROM userData WHERE userId='{rs[0][0]}'")
                    rs_data=cursor.fetchall()
                    session['creationDate']=rs_data[0][3]
                    session['lastLogin']=rs_data[0][4]
                    session['nom']=rs_data[0][1]
                    session['prenom']=rs_data[0][2]
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
            hashedPwd=bc.generate_password_hash(password).decode("utf-8")
            sql="INSERT INTO user (email,password) VALUES (%s,%s)"
            val=(email,hashedPwd)
            cursor.execute(sql,val)
            id=cursor.lastrowid
            sql2="INSERT INTO userdata (userId,nom,prenom,creationDate,lastLogin) VALUES (%s,%s,%s,CURDATE(),CURDATE())"
            val2=(int(id),nom,prenom)
            cursor.execute(sql2,val2)
            db.commit()
            session['nom']=nom
            session['prenom']=prenom
            session['email']=email
            session['password']=password
            session['creationDate']=datetime.datetime.today
            session['lastLogin']=datetime.datetime.today
            session['logged']=True
            return redirect("/dashboard",code=301)
        except Exception as e:
            return redirect("/",code=303)
    return redirect("/",code=303)


@app_views.route('/logout',strict_slashes=False)
def logout():
    cursor.execute(f"UPDATE `userdata` SET `lastLogin`=CURDATE() WHERE userId = (SELECT userId from user where email='{session['email']}')")
    db.commit()
    session['logged']=False
    return redirect('/',code=303)



@app_views.route('/changePassword',strict_slashes=False,methods=['POST'])
def changePassword():
    password=request.form.get('current_password')
    newPassword=request.form.get('new_password')
    if password==session['password']:
        hashedPwd=bc.generate_password_hash(newPassword).decode('utf-8')
        sql=f"UPDATE user SET password='{hashedPwd}' where email='{session['email']}'"
        cursor.execute(sql)
        db.commit()
        return render_template('accounts/profileChanged.html')

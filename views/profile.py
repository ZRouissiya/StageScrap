from flask import render_template,session,redirect,abort,request
from views  import app_views
import pickle

@app_views.route("/profile",strict_slashes=False)
def profile():
    if 'user' in session:
        currentUser=session['user']
        if currentUser:
            user=pickle.loads(currentUser)
            return render_template("accounts/profile.html",fullname=user.fullname(),nom=user.lastName,prenom=user.name,email=user.email,lastLogin=user.lastLogin,creationDate=user.createDate)
        return redirect('/',code=303)
    else:
        return abort(401)
    
@app_views.route('/changePassword',strict_slashes=False,methods=['POST'])
def changePassword():
    password=request.form.get('current_password')
    newPassword=request.form.get('new_password')
    if 'user' in session:
        try:
            currentUser=session['user']
            user=pickle.loads(currentUser)
            if password==user.password:
                if user.updatePassword(newPassword):
                    return render_template('accounts/profileChanged.html',fullname=user.fullname(),nom=user.lastName,prenom=user.name,email=user.email,lastLogin=user.lastLogin,creationDate=user.createDate),200 
            return render_template('accounts/profileError.html',fullname=user.fullname(),nom=user.lastName,prenom=user.name,email=user.email,lastLogin=user.lastLogin,creationDate=user.createDate), 301
        except Exception as e:
            return render_template('accounts/profileError.html',fullname=user.fullname(),nom=user.lastName,prenom=user.name,email=user.email,lastLogin=user.lastLogin,creationDate=user.createDate),302
    return abort(500)

@app_views.route('/updateData', methods=['POST'],strict_slashes=False)
def updateData():
    prenom=request.form.get('prenom')
    nom=request.form.get('nom')
    email=request.form.get('email')
    if 'user' in session:
        currentUser=session['user']
        userPre=pickle.loads(currentUser)
        if userPre.updateData(prenom,nom,email)==1:
            session['user']=pickle.dumps(userPre)
            user=pickle.loads(session['user'])
            return render_template('accounts/profileChanged.html',fullname=user.fullname(),nom=user.lastName,prenom=user.name,email=user.email,lastLogin=user.lastLogin,creationDate=user.createDate),200
        elif userPre.updateData(prenom,nom,email)==0:
            return render_template('accounts/profileErrorEmail.html',fullname=userPre.fullname(),nom=userPre.lastName,prenom=userPre.name,email=userPre.email,lastLogin=userPre.lastLogin,creationDate=userPre.createDate),301   
    return render_template('accounts/profileError.html',fullname=userPre.fullname(),nom=userPre.lastName,prenom=userPre.name,email=userPre.email,lastLogin=userPre.lastLogin,creationDate=userPre.createDate),302


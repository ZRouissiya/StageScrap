import mysql.connector as con
from flask_bcrypt import Bcrypt
db=con.connect(host="localhost",user="root",password="",database='db_stage')
cursor=db.cursor()
bc=Bcrypt()

class user():
    def __init__(self,name,lastName,email,password,userId=None):
        self.name=name
        self.lastName=lastName
        self.email=email
        self.password=password
        if userId is None:
            self.userId=self.insert(name,lastName,email,password)


    def insert(self,name,lastName,email,password):
        hashedPwd=bc.generate_password_hash(password).decode("utf-8")
        sql="INSERT INTO user (email,password) VALUES (%s,%s)"
        val=(email,hashedPwd)
        cursor.execute(sql,val)
        id=cursor.lastrowid
        sql2="INSERT INTO userdata (userId,nom,prenom,creationDate,lastLogin) VALUES (%s,%s,%s,CURDATE(),CURDATE())"
        val2=(int(id),lastName,name)
        cursor.execute(sql2,val2)
        db.commit()
        return id
     
    def updateData(self,name,lastName,email):
        cursor.execute(f"SELECT * FROM user WHERE email='{email}'")
        rs=cursor.fetchall()
        if email!=self.email and len(rs)==0:
            try:
                cursor.execute(f"UPDATE `user` SET `email`='{email}' WHERE email='{self.email}'")
                self.email=email
                if len(lastName)==0 and len(name)==0 :
                    sql=f"UPDATE `userdata` SET `nom`='{lastName}',`prenom`='{name}' WHERE userId = {self.userId}')"
                    cursor.execute(sql)
                    self.name=name
                    self.lastName=lastName
                    self.email=email
                    db.commit()
                    return True
                return False
            except Exception as e:
                return False

    
    def updatePassword(self,newPassword):
        hashedPwd=bc.generate_password_hash(newPassword).decode('utf-8')
        sql=f"UPDATE user SET password='{hashedPwd}' where email='{self.email}'"
        cursor.execute(sql)
        db.commit()
     
    def logOut(self):
        del self
import mysql.connector as con
from flask_bcrypt import Bcrypt
import datetime
db=con.connect(host="localhost",user="root",password="",database='db_stage')
cursor=db.cursor()
bc=Bcrypt()

class User():
    def __init__(self,name,lastName,email,password,createDate=datetime.datetime.today().strftime('%d-%m-%Y'),lastLogin=datetime.datetime.today().strftime('%d-%m-%Y'),userId=None):
        self.name=name
        self.lastName=lastName
        self.email=email
        self.password=password
        self.createDate=createDate
        self.lastLogin=lastLogin
        self.userId=userId
    def fullname(self):
        return self.name +' '+self.lastName
    def insert(self):
        try:
            hashedPwd=bc.generate_password_hash(self.password).decode("utf-8")
            sql="INSERT INTO user (email,password) VALUES (%s,%s)"
            val=(self.email,hashedPwd)
            cursor.execute(sql,val)
            id=cursor.lastrowid
            sql2="INSERT INTO userdata (userId,nom,prenom,creationDate,lastLogin) VALUES (%s,%s,%s,CURDATE(),CURDATE())"
            val2=(int(id),self.lastName,self.name)
            cursor.execute(sql2,val2)
            db.commit()
            self.userId=id
            return True
        except Exception as e:
            return False
        
    def updateData(self,name,lastName,email):
        cursor.execute(f"SELECT * FROM user WHERE email='{email}'")
        rs=cursor.fetchall()
        if len(rs)==1:
            if self.email==rs[0][1]:
                if self.updateToDb(name,lastName,email):
                    
                    return 1
                return -1
            else:
                return 0
        if email!=self.email and len(rs)==0:
            self.updateToDb(name,lastName,email)
            return 1
        return -1

    
    def updatePassword(self,newPassword):
        try:
            hashedPwd=bc.generate_password_hash(newPassword).decode('utf-8')
            sql=f"UPDATE user SET password='{hashedPwd}' where email='{self.email}'"
            cursor.execute(sql)
            db.commit()
            return True
        except Exception as e:
            return False   
        
          
    def logOut(self):
        try:
            cursor.execute(f"UPDATE `userdata` SET `lastLogin`=CURDATE() WHERE userId = (SELECT userId from user where email='{self.email}')")
            db.commit()
            del self
            return True
        except Exception as ex:
            return False
        
    def updateToDb(self,name,lastName,email):
        try:
                cursor.execute(f"UPDATE `user` SET `email`='{email}' WHERE email='{self.email}'")
                self.email=email
                if len(lastName)!=0 and len(name)!=0 :
                    sql=f"UPDATE `userdata` SET `nom`='{lastName}',`prenom`='{name}' WHERE userId = {self.userId}"
                    cursor.execute(sql)
                    self.name=name
                    self.lastName=lastName
                    self.email=email
                    db.commit()
                    return True
                return False
        except Exception as e:
            return False
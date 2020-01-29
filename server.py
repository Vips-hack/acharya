from flask import Flask,request,redirect,url_for
from firebase_admin import credentials, db
import firebase_admin
#import firebase_data
app = Flask(__name__)

################################################################################
##################### FIREBASE CREDENTIALS #####################################

####################FIREBASE CREDENTIALS########################################
################################################################################



def upload_data(*data):
    ref = db.reference("user_cred")
    child=ref.child(str(data[1]))
    child.set({
        "email": data[0],
        "password": data[1],
        "username": data[2],
        "number": data[3],
        "institute": data[4],
        "qualification": data[5]
    })

    
def check_cred(email,password):
    ref=db.reference("user_cred")
    if str(ref.child(str(email)).get()) != "None":
        child=ref.child(str(email))
        data=child.get()
        if data["password"] == password:
            return True
        else:
            return False
    else:
        return False
    


@app.route("/register")
def register():
    email=request.form.get("email")
    password=request.form.get("password")
    username=request.form.get("username")
    number=request.form.get("number")
    institute=request.form.get("institute")
    qualification=request.form.get("qualification")
    upload_data(email,password,username,number,institute,qualification)
    redirect(url_for( login() ) )

@app.route('/login')
def login():
    email=request.form.get("email")
    password = request.form.get("password")
    login_type= check_cred(email,password)
    if login_type:
        redirect("file:///E:/vips/vips/Aacharya-master/mIainpage.html")
    else:
        return "Goli beta Mastiii nhiiiii"
    return "done"


if __name__ == "__main__":
    app.run(debug=True)
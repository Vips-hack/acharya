from flask import Flask,request,redirect,url_for,render_template
from firebase_admin import credentials, db
import firebase_admin
#import firebase_data
app = Flask(__name__)

################################################################################
##################### FIREBASE CREDENTIALS #####################################
cred = credentials.Certificate(r'C:\Users\jain\Downloads\vips-hack-firebase-adminsdk-de023-b4d860fd84.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vips-hack.firebaseio.com/'
})

####################FIREBASE CREDENTIALS########################################
################################################################################



def upload_data(*data):
    ref = db.reference("temp")
    child=ref.child(str(data[0]))
    child.set({
        "email": str(data[0]),
        "password": str(data[1]),
        "username": str(data[2]),
        "number": str(data[3]),
        "institute": str(data[4]),
        "qualification": str(data[5])
    })

    
def check_cred(email,password):
    ref=db.reference("temp")
    if str(ref.child(str(email)).get()) != "None":
        child=ref.child(str(email))
        data=child.get()
        if data["password"] == str(password):
            return True
        else:
            return False
    else:
        return False
    


@app.route("/register", methods = ["POST"])
def register():
    email=request.form.get("email")
    password=request.form.get("password")
    username=request.form.get("username")
    number=request.form.get("number")
    institute=request.form.get("institute")
    qualification=request.form.get("qualification")
    upload_data(email,password,username,number,institute,qualification)
    return render_template( "a (1).html")

@app.route('/login', methods = ["POST","GET"])
def login():

    email=request.form.get("email")
    password = request.form.get("password")
    login_type= check_cred(email,password)
    if login_type:
        return render_template("mIainpage.html")
    else:
#        return render_template("a(1).html")
        return render_template( "a (1).html")
#        return "invalid credentials"


if __name__ == "__main__":
    app.run(debug=True)
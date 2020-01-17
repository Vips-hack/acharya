import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'C:\Users\jain\Downloads\vips-hack-firebase-adminsdk-de023-b4d860fd84.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vips-hack.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref=db.reference("student")
#ref_child=ref.child(str(input("department")))
ref_child=ref.child("department")
#ref_child_class=ref_child.child(str(input("class")))
#ref_child_class_student_cred=ref_child_class.child(str(input("student cred")))
ref_child_class=ref_child.child("a")
ref_child_class_student_cred=ref_child_class.child("student_cred")

while(str(input("contunue data update")) == "t"):
    ref_child_class_student_cred.set({

    "name":str(input("enter student name")),
    "roll-no": int(input("enter student roll no")),
    "email-id": str(input("enter student email-id")),
    "attendance percentage":str(input("enter student attandance percentage")),
    "today`s attandance":int(input("is he present today- 1 for present and 0 for absent"))

})
'''
ref_child_student-cred.set({"name":name,
"roll-no":roll-no,
"email-id": email})

#student_ref=ref.child("cse")
#student_ref.set({"name":"sanskar jain",
#                "email-id":"sanskar@gmail.com",
#                "roll-no":"12"})

ref = db.reference('server/saving-data/fireblog')
users_ref = ref.child('users')
users_ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})
users_ref.child('alanisawesome').set({
    'date_of_birth': 'June 23, 1912',
    'full_name': 'Alan Turing'
})
users_ref.child('gracehop').set({
    'date_of_birth': 'yo 9, 1906',
    'full_name': 'Grace Hopper'
})
hopper_ref = users_ref.child('gracehop')
hopper_ref.update({
    'nickname': 'Amazing Grace'
})
users_ref.update({
    'alanisawesome/nickname': 'Alan The Machine',
    'gracehop/nickname': 'Amazing Grace'
})
users_ref.update({
    'alanisawesome': {
        'nickname': 'Alan The Machine'
    },
    'gracehop': {
        'nickname': 'Amazing Grace'
    
})'''
json=ref_child_class_student_cred.get()
print(type(json))
df=pandas.DataFrame.from_dict(json,orient="index")

print(df.loc["email-id",0])
#print(ref_child_class_student_cred.get())
#print(ref_child_class.child.get())
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import tabula
import pandas as pd
import openpyxl
from tabulate import tabulate
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'C:\Users\nisha\Downloads\aacharyabitrebels-firebase-adminsdk-b42s8-871c876289.json')


# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aacharyabitrebels.firebaseio.com/'
})

class teacher :
    def __init__(teacher, name , email, department, tclass,ttype,subject):
        teacher.name = name
        teacher.email = email
        teacher.department = department
        teacher.tclass = tclass
        teacher.ttype = ttype
        teacher.subject = subject

    #a function to store values at the time of regiteration
    def register():
       teacher_name = str(input("NAME :- "))
       teacher_email =str(input("EMAIL :- "))
       teacher_department = str(input("CSE / ECE / IT / MECH / EEE"))
       teacher_class = input("CLASS  :-")
       teacher_type = str(input("TEACHER / PROCTOR"))
       teacher_sub = str(input("SUBJECT"))
                                    #dekhlio be 

   # TO FIND ANY FREE PERIOD IF AVAILABLE
    def time_table_examine (time_table_link):
        df = tabula.read_pdf(r"%s"%(time_table_link), pages='1',multiple_tables=True)
        tabula.convert_into(r"%s"%(time_table_link), "Output.csv", output_format="csv", pages='1')
        read_csv_file= pd.read_csv("Output.csv")
        read_csv_file.to_excel("ExcelIndo.xlsx", index = None, header = True)
        time_table = xlrd.open_workbook('ExcelIndo.xlsx')
        sheet =time_table.sheet_by_index(0)
        sheet.cell_value(0, 0)
        for i in range(sheet.nrows):
            for j in range(sheet.ncolumns):
                if(sheet.cvbell_value(i, j)== "FREE")or (sheet.cvbell_value(i, j)== "free"):
                    print("Want an arrangement period / or any any meeting with parents ?")




    def upload_data_firebase():
        ans ='y'
     # As an admin, the app has access to read and write all data, regradless of Security Rules
        ref=db.reference("%s" %(teacher_class))
        ref_class=ref.child("STUDENT DATA")
        while(ans== "y"):
            student_name = str(input("Enter the name of student :- "))
            student_rollno = int(input("Enter the roll no of student :- "))
            student_email = input("Enter the email address of the student :-")
            student_phoneno = input("Enter the phone number of the student :-")
            ref_class_studentdata=ref_class.child("%d"%(student_rollno))
            ref_class_studentdata.set({
                 "NAME":student_name,
                 "ROLL NO": student_rollno,
                 "EMAIL":student_email,
                 "PHONE NO" : student_phoneno
         })
            ans=str(input("Want to continue ? (y/n)"))

        

    def send_assignment():
        no_assignment = int(input("Enter the no of assignment :- ")
        ass_due_date = str(input("Enter the last date of submission :- "))
        assignment_loc = input("Enter the path of file ")
      #write code to upload file to cloud 
        no_students = int (input("Enter the total no of students"))
        for i in range (1,no_students):
            json=ref_class_studentdata.get()
            df=pd.DataFrame.from_dict(json,orient="index")
            stu_email= df.loc["email-id",0])
            subject = "Assignment"+no_assignment
            body = "Last date of submission of this assignment is " +last_day_of_submis
            sender_email = teacher_email
            receiver_email = stu_email
            password = input("Type your password and press enter:")

          # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails
 
          # Add body to email
            message.attach(MIMEText(body, "plain"))

            filename = "WRITE COODE HERE TO DOWNLOAD THE FILE FROM cloudstorage"  # Write code to download the assignment code from cloud

         # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
              # Add file as application/octet-stream
              # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

         # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

         # Add header as key/value pair to attachment part
            part.add_header(
          "Content-Disposition",
          f"attachment filename= {filename}",
          )

          # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()

          # Log in to server using secure context and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
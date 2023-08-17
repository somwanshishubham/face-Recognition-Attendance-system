import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("#####")
firebase_admin.initialize_app(cred, {
    "databaseURL": "#######"
})

# create a reference for adding data
ref = db.reference("Students")

while True:
    rollNo = input("\nPlease Enter Your Roll No & for Exit press -1:")

    if rollNo == '-1':
        break
    pass

    nameVar = input("Please Enter Your Name :")
    clas = input("Please Enter Your class :")
    dp_name = input("Please Enter Your Department Name :")
    year = input("Please Enter Your Current Studying Year :")
    admission_yr = input("please Enter Your Admission Year :")
    #lec_time = input("Enter Lecture Name & Time :")

    data = {
        'name': nameVar,
        'roll_no': rollNo,
        'class': clas,
        '2 to 3': "A",
        '3 to 4': "A",
        '4 to 5': "A",
        'department_name': dp_name,
        'cr_year': year,
        'admission_year': admission_yr,
        #'lec_time': lec_time,
        'last_attendance_time': "2023-5-7, 09:46:59",
        'total_attendance': 0
    }

    ref.child(rollNo).set(data)
pass
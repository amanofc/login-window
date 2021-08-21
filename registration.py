# Run this program from "welcome.py" file
# create a table for employee(Emp_id int(11), Emp_name varchar(256), Emp_sal int(5), Emp_doj date)
# create another table for registration(user_id int(11) primary key, username varchar(256), password varchar(256), email varchar(256), phone int(11), dob date)


def registrationPage():
    import mysql.connector as mysql
    db = mysql.connect(host='localhost', user='root', port='3306', database='demo')
    print("*************************** Registration Page **************************")
    while(1):
        try:
            user_id = int(input("Enter the user_id:"))
            username = input("Enter username:")
            password = input("Enter password:")
            email = input("Enter your email id:")
            phone = int(input("Enter phone number:"))
            dob =input("Enter your date of birth:")
            break
        except ValueError:
            print("Enter Number!")


    cur = db.cursor()
    cmd = "insert into Registration values(%s,%s,%s,%s,%s,%s)"
    args = (user_id, username, password, email, phone, dob)
    cur.execute(cmd, args)
    db.commit()
    print("SIGN UP SUCCESSFUL !!")
    print("*********************************************************************")
    db.close()





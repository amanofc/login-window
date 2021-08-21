# Run this program from "welcome.py" file
# create a table for employee(Emp_id int(11), Emp_name varchar(256), Emp_sal int(5), Emp_doj date)
# create another table for registration(user_id int(11) primary key, username varchar(256), password varchar(256), email varchar(256), phone int(11), dob date)

import mysql.connector as mysql

from project.userProfile import profile

db = mysql.connect(host='localhost', user='root', port='3306', database='demo')
cur = db.cursor()


def insertTable():
    print("***************************Inserting Data**************************")
    while(1):
        try:
            Emp_id = int(input("Enter the Employee id:"))
            Emp_name = input("Enter the Employee Name:")
            Emp_sal = int(input("Enter the Employee Salary:"))
            Emp_doj = input("Enter the Employee date of joining:")
            cur.execute("insert into Employee values (%s,%s,%s,%s)",(Emp_id, Emp_name, Emp_sal, Emp_doj))
            db.commit()
            print("data updated.\n")
            break
        except ValueError:
            print("Enter only Numbers!\n")
        except mysql.connection.errors.IntegrityError:
            print("Employee ID already exist! Try again.\n")


def updateTable():
    print("***************************Updating Data**************************")
    while(1):
        try:
            id = input("Enter the Employee id:")
            name = input("Enter the Employee Name:")
            sal = input("Enter the Employee Salary:")
            doj = input("Enter the Employee date of joining:")
            cur.execute("update employee set Emp_name='"+name+"',Emp_salary="+sal+",doj='"+doj+"' where Emp_id="+id+"")
            db.commit()
            print("data updated")
            break
        except mysql.connection.errors.ProgrammingError:
            print("Enter Number!\n")

def deleteTable():
    print("***************************Deleting Data**************************")
    while(1):
        try:
            Emp_id = (input("enter the Emp_id:"))
            cur.execute("delete from employee where Emp_id="+Emp_id+"")
            db.commit()
            print("data deleted")
            break
        except mysql.connection.errors.ProgrammingError:
            print("Enter only Number!\n")

def showTables():
    print("*************************** Employees Detail **************************")
    cur.execute("select * from Employee")
    print("Emp_Id\t\tName\t\t\tSalary\t\t\tDOJ")
    for i in cur:
        for j in i:
            print(j, end="\t\t\t")
        print()

def searchTable():
    print("***************************Searching Data**************************")
    while(1):
        try:
            id = input("Enter the Employee id:")
            cur.execute("select * from Employee where Emp_id="+id+"")
            print("Emp_Id\t\tName\t\t\tSalary\t\t\tDOJ")
            for i in cur:
                for j in i:
                    print(j, end="\t\t\t")
            print()
            break
        except mysql.connection.errors.ProgrammingError:
            print("Enter only Number!\n")

def loginPage():
    while(1):
        print("*************************** Login Page **************************")
        username = input("Enter the user name:")
        password = input("Enter the password:")
        cmd = "select username,password from registration where username=%s and password=%s"
        parameters = (username, password)
        cur.execute(cmd, parameters)
        res = cur.fetchone()
        if res:
            print("*************************** Welcome", res[0], "**************************")
            while (1):
                print("\ninsert=1\nupdate=2\ndelete=3\nshow_data=4\nsearch_id=5\n\nExit=0\nGo to Profile Page=10")
                while(1):
                    try:
                        choice = int(input("\nEnter your Option:"))
                        break
                    except ValueError:
                        print("Enter Only Number!\n")
                if choice == 1:
                    insertTable()

                elif choice == 2:
                    updateTable()

                elif choice == 3:
                    deleteTable()

                elif choice == 4:
                    showTables()

                elif choice == 5:
                    searchTable()

                elif choice==10:
                    while(1):
                        profile()
                        break




                elif choice == 0:
                    break
                else:
                    print("Invalid Option!\n")


        else:
            print("Invalid Username / Password!\n")

    db.close()
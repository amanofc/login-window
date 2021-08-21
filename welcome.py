                                                    #Main file..
# create a table for employee(Emp_id int(11), Emp_name varchar(256), Emp_sal int(5), Emp_doj date)
# create another table for registration(user_id int(11) primary key, username varchar(256), password varchar(256), email varchar(256), phone int(11), dob date)

import mysql.connector as mysql
try:
    from project.login import loginPage
    from project.registration import registrationPage

    print("***************************** Welcome ****************************\n")
    print("Login=1\t\t\t\tRegister=2")

    while (1):
        try:
            option = int(input("\nSelect Option:"))
            if option > 2:
                print("Enter a valid Option!")
                continue
            else:
                break
        except ValueError:
            print("Enter number!")

    if option == 1:
        loginPage()
    elif option == 2:
        registrationPage()

except mysql.connection.errors.InterfaceError:
    print("Database Connection Failed! Check Coonection. .")
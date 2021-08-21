import mysql.connector as mysql
db = mysql.connect(host='localhost', user='root', port='3306', database='demo')
cur = db.cursor()

List=[]
def editProfile():
    print("hello")


def editProfileOption():
    print("Edit Profile=1")
    print("Go to Main Page=0")
    while(1):
        try:
            option = int(input("\nSelect Option:"))
            if option==1:
                editProfile()
            elif option==0:
                print("*************************** Welcome", List[1], "**************************")
                break
            else:
                print("Invalid Option!")


        except ValueError:
            print("Enter Number Only!")


def profile():
    while(1):
        print("*************************** Profile Page **************************")
        id =input("Enter Your Used ID:")
        password = input("Enter Passsword:")
        cur.execute= "select username from registration where user_id="+id+" and password='"+password+"'"
        res = cur.fetchone()
        print("res=",res)
        if res:
            print("***************************",res[1],"'s Profile **************************")
            print("\nUser_id\t\tUsername\t\tPassword\t\t\tEmail\t\t\t\t\t\tPhone\t\t\t\tDOB")
            for i in cur:
                print(i)
                for j in i:
                    print(j, end="\t\t\t")
            print()
            editProfileOption()
            break
        else:
            print("Invalid User ID / Password! Try Again. .")



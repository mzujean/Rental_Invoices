# from asyncio.proactor_events import _ProactorSocketTransport
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port= 3306,
  user="root",
  password="45?:.4coD$",
#   database="Rental_Invoices.sql"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")


mydb.commit()

for x in mycursor:
  print(x)


def make_login_details():
    print("Create a login and password")
    username = input("Input username: ")
    password = input("Input password: ")
    password_check = input("Confirm password: ")

    if (password == password_check):
        result1 = "Username: "+ " " + username
        result2 = "Password: "+" "+ password
        return result1 + " \n" + result2
    else:
        password = input("Input password: ")
        password_check = input("Confirm password: ")




# checks if information captured is correct. If it is not correct
# it takes you back to filling out your details from the beginning


def if_info_captured():
    select = input("y / n: ")
    if (select == "n"):
        print(name_captured())
    elif (select == "y"):
        print("You're information is saved. Please set up your sign up details.")

        print(make_login_details())
        # go to sign in page from here



# aCptures the details of the tenant

def name_captured():

    print("_____Please fill in the following details below_____")
    first_name = input("First name: ")
    surname = input("Surname: ")
    cellphone_number = int(input("Cell Number: "))
    id_No = int(input("ID No( if South African otherwise insert 0): "))
    passport = input("Passport: ")
    email_address = input("Email Address: ")

    print(first_name)
    print(surname)
    print(cellphone_number)
    print(id_No)
    print(passport)
    print(email_address)
    print("Please check information captured is correct. You will be unable to change it from here on")

    return if_info_captured()


#print(name_captured())

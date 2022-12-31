import tkinter as tk
from tkinter.ttk import *
import mysql.connector
from datetime import datetime
#from tk import StringVar
from tk import *

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Anu@2001",
  database ="library"
)

db=mydb.cursor()
root = tk.Tk()
def loginFN(user,pwd):
    
    try:

        find_user_query="select * from user where user_id=%s and password=%s"
        adr = (user,pwd)
        db.execute(find_user_query,adr)
        user  = db.fetchone()

        if user==None:
            return "Invalid Credentials"
        else:
            return {"user_id":user[0],"name":user[1],"Phone":user[2],"dept":user[4],"admin_year":user[5]}
        
    except mysql.connector.Error as err:
        print(err)
        return "Unexpected Error Occurred"



def Loginform():
    global login_screen
    login_screen = tk()
    #Setting title of screen
    login_screen.title("Login Form")
    #setting height and width of screen
    login_screen.geometry("300x250")
    #declaring variable
    global user
    global pwd
    global  message;
    user = tk.StringVar()
    pwd = tk.StringVar()
    message=tk.StringVar()

#Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(login_screen, text="Username * ").place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=user).place(x=90,y=42)
    #Password Label
    Label(login_screen, text="Password * ").place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=pwd ,show="*").place(x=90,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=loginFN).place(x=105,y=130)
    login_screen.mainloop()
#calling function Loginform
Loginform()
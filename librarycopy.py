import tkinter as tk
from tkinter import *
from PIL import ImageTk
from tkinter import ttk
import mysql.connector
from datetime import datetime
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database ="library"
)

db=mydb.cursor()





def book_listFN():

    try:

        find_book_query="select * from book where status=%s"
        adr=("not issued",)
    
        
        db.execute(find_book_query,adr)
        book = db.fetchall()
        print(book)

        if len(book)==0:
            return []
        else:
            return book
    except mysql.connector.Error as err:
        print(err)
        return "Unexpected Error Occurred"
#book_listFN()


def book_addFN(book_id,user_id):

    try:
        change_status_query="update book set status=%s where book_id=%s"
        adr=("issued",book_id)
       
        db.execute(change_status_query,adr)
        mydb.commit()
        now = datetime.now()
        id = 1
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        add_book_query="insert into Borrowed values(%s,%s,%s)"
        adr=(book_id,user_id,formatted_date)
        db.execute(add_book_query,adr)
        mydb.commit()
        return True

       
    except mysql.connector.Error as err:
        print(err)
        return "Unexpected Error Occurred"

#book_addFN("25","20br13455")
    


def profileFn(user_id):
    try:

        user_details_query="select user_id,name,ph_no,admin_year,dept from user where user_id=%s"
        adr=(user_id,)
        db.execute(user_details_query,adr)
        user = db.fetchone()

        book_details_query="select book.* from book natural join Borrowed where user_id=%s"
        adr=(user_id,)
        db.execute(book_details_query,adr)
        books = db.fetchall()

        return {"user_data":user,"books_details":books}

    except mysql.connector.Error as err:
        print(err)
        return "Unexpected Error Occurred"
#a= profileFn("20br13455")
#print(a)




#         ----------------------------------------  app -----------------------------------------------
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, SignupPage,PageOne,BooksPage,ProfilePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#---------------------------------------------------------- Login -------------------------------------------------

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load the image file
        self.image = PhotoImage(file="bg.png")
        
        # Create a label to display the image
        self.label = ttk.Label(self, image=self.image)
        self.label.pack()

        def user_enter(event):
            if userEntry.get()=='Username':
                userEntry.delete(0,END)

        def pwd_enter(event):
            if pwdEntry.get()=='Password':
                pwdEntry.delete(0,END)

        def hide():
            openeye.config(file='closeye.png')
            pwdEntry.config(show='*')
            eyebutton.config(command=show)

        def show():
            openeye.config(file='openeye.png')
            pwdEntry.config(show='')
            eyebutton.config(command=hide) 

        def loginFN(user,pwd):
            self.user1=user
            self.pass1=pwd
        
            try:
                find_user_query="select * from user where user_id='"+self.user1+"' and password='"+self.pass1+"'"
                adr = (user,pwd)
                db.execute(find_user_query,adr)
                user  = db.fetchone()

                if user==None:
                    controller.show_frame(PageOne)
                    return "Invalid Credentials"
                else:
                    controller.show_frame(PageOne)
                    return {"user_id":user[0],"name":user[1],"Phone":user[2],"dept":user[4],"admin_year":user[5]}
                
            except mysql.connector.Error as err:
                print(err)
                return "Unexpected Error Occurred"

        

        heading=Label(self,text='USER LOGIN',font=('Microsoft Yehei UI Light',23,'bold'),bg='white',fg='firebrick2')
        heading.place(x=605,y=120)

        userEntry=Entry(self,width=25,font=('Microsoft Yehei UI Light',11,'bold'),bg='white',bd=0,fg='firebrick2')
        userEntry.place(x=580,y=200)
        userEntry.insert(0,'User Id')

        userEntry.bind('<FocusIn>',user_enter)

        frame1=Frame(self,width=250,height=2,bg='firebrick1').place(x=580,y=222)

        pwdEntry=Entry(self,width=25,font=('Microsoft Yehei UI Light',11,'bold'),bg='white',bd=0,fg='firebrick2')
        pwdEntry.place(x=580,y=300)
        pwdEntry.insert(0,'Password')
        pwdEntry.bind('<FocusIn>',pwd_enter)
        frame2=Frame(self,width=250,height=2,bg='firebrick1').place(x=580,y=322)

        openeye=PhotoImage(file='openeye.png')
        eyebutton=Button(self,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
        eyebutton.place(x=800,y=290)

        loginButton =Button(self,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1',activeforeground='white',cursor='hand2',bd=0,width=19,command= lambda: controller.show_frame(PageOne))
        loginButton.place(x=588,y=380)

        signupLabel = Label(self,text="Don't have an account?",font=('Open Sans',10),fg='firebrick1',bg='white')
        signupLabel.place(x=580,y=450)

        newaccountButton =Button(self,text='create new account',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activebackground='blue',activeforeground='white',cursor='hand2',bd=0,
        command=lambda: controller.show_frame(SignupPage))
        newaccountButton.place(x=727,y=450)
    
    



#---------------------------------------------------------SignUp--------------------------------------------------------


class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        def clear():
            useridEntry.delete(0,END)
            usernameEntry.delete(0,END)
            phnoEntry.delete(0,END)
            pwdEntry.delete(0,END)
            deptEntry.delete(0,END)
            admyearEntry.delete(0,END)

        def connect_database():
            if useridEntry.get()=='' or usernameEntry.get()=='' or pwdEntry.get()=='' or phnoEntry.get()=='' or deptEntry.get()=='' or admyearEntry.get()=='':
                messagebox.showerror('Error','All Fields are Required')
            else :
                registerFN()
        def registerFN():
            try:
                add_user_query="insert into user values(%s,%s,%s,%s,%s,%s)"
                adr = (useridEntry.get(), usernameEntry.get(),phnoEntry.get(),pwdEntry.get(),deptEntry.get(),admyearEntry.get())
                db.execute(add_user_query,adr)
                mydb.commit()
                messagebox.showinfo('Sucess','Registration is sucessfull')
                clear()
                self.destroy()
                controller.show_frame(LoginPage)
                return True

            except mysql.connector.Error as err:
                print(err)
                return False



    #registerFN(("20br13455","Anu","9999944678","ab@134","cse","2020"))

    #a =loginFN("20br13455","ab@134")
    #print(a)    
                


        # Load the image file
        self.image = PhotoImage(file="bg.png")
        
        # Create a label to display the image
        self.label = ttk.Label(self, image=self.image)
        self.label.pack()


        frame=Frame(self,bg='white')
        frame.place(x=554,y=100)


        heading=Label(frame,text="CREATE AN ACCOUNT ",font=('Microsoft Yehei UI Light',18,'bold'),bg='white',fg='firebrick2')
        heading.grid(row=0,column=0,padx=10,pady=10)

        #userid
        useridlabel=Label(frame,text="User Id : ",font=('Microsoft Yehei UI Light',10,'bold'),bg='white',fg='firebrick2')
        useridlabel.grid(row=1,column=0,sticky='w',padx=25)

        useridEntry=Entry(frame,width=25,font=('Microsoft Yehei UI Light',10,'bold'),bg='light pink',fg='DeepPink4')
        useridEntry.grid(row=2,column=0,sticky='w',padx=25)

        #username
        usernamelabel=Label(frame,text="User Name : ",font=('Microsoft Yehei UI Light',10,'bold'),bg='white',fg='firebrick2')
        usernamelabel.grid(row=3,column=0,sticky='w',padx=25,pady=(5,0))

        usernameEntry=Entry(frame,width=25,font=('Microsoft Yehei UI Light',10,'bold'),bg='light pink',fg='DeepPink4')
        usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

        #password
        pwdlabel=Label(frame,text="Password : ",font=('Microsoft Yehei UI Light',10,'bold'),bg='white',fg='firebrick2')
        pwdlabel.grid(row=5,column=0,sticky='w',padx=25,pady=(5,0))

        pwdEntry=Entry(frame,width=25,font=('Microsoft Yehei UI Light',10,'bold'),bg='light pink',fg='DeepPink4')
        pwdEntry.grid(row=6,column=0,sticky='w',padx=25)

        #phone no
        phnolabel=Label(frame,text="Phone No : ",font=('Microsoft Yehei UI Light',10,'bold'),bg='white',fg='firebrick2')
        phnolabel.grid(row=7,column=0,sticky='w',padx=25,pady=(5,0))

        phnoEntry=Entry(frame,width=25,font=('Microsoft Yehei UI Light',10,'bold'),bg='light pink',fg='DeepPink4')
        phnoEntry.grid(row=8,column=0,sticky='w',padx=25)

        #dept
        deptlabel=Label(frame,text="Department : ",font=('Microsoft Yehei UI Light',10,'bold'),bg='white',fg='firebrick2')
        deptlabel.grid(row=9,column=0,sticky='w',padx=25,pady=(5,0))

        deptEntry=Entry(frame,width=25,font=('Microsoft Yehei UI Light',10,'bold'),bg='light pink',fg='DeepPink4')
        deptEntry.grid(row=10,column=0,sticky='w',padx=25)

        #adm year
        admyearlabel=Label(frame,text="Admission Year : ",font=('Microsoft Yehei UI Light',10,'bold'),bg='white',fg='firebrick2')
        admyearlabel.grid(row=11,column=0,sticky='w',padx=25,pady=(5,0))

        admyearEntry=Entry(frame,width=25,font=('Microsoft Yehei UI Light',10,'bold'),bg='light pink',fg='DeepPink4')
        admyearEntry.grid(row=12,column=0,sticky='w',padx=25)


        signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',
                            activebackground='firebrick1',activeforeground='white',command=connect_database)
        signupButton.grid(row=13,column=0,padx=25,pady=(10,0),sticky='w')

        loginLabel = Label(self,text="Alredy have an account?",font=('Open Sans',10),fg='firebrick1',bg='white')
        loginLabel.place(x=580,y=500)

        loginButton =Button(self,text='Login',font=('Open Sans',9,'bold underline'),
        fg='blue',bg='white',activebackground='blue',activeforeground='white',cursor='hand2',bd=0,command= lambda: controller.show_frame(LoginPage))
        loginButton.place(x=730,y=500)

#------------------------------------------NEXT PAGES ----------------------------------- 
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load the image file
        self.image = PhotoImage(file="bgoo.png")
        
        # Create a label to display the image
        self.label = ttk.Label(self, image=self.image)
        self.label.pack()     
        self.title = Label(self, text="DASHBOARD", font=(
            'Microsoft Yehei UI Light', 16, 'bold'),bg='pink')
        self.title.place(x=450, y=60)
        frame=Frame(self,bg='white')
        frame.place(x=200,y=100) 
        b1 = tk.Button(frame, text="Add User",
                            command=lambda: controller.show_frame(SignupPage),bg='deeppink',fg='white',font=('Open Sans',16,'bold'))
        b1.grid(row=1,column=0,padx=225,pady=25)                    
        
        b2 = tk.Button(frame, text="View Books",
                            command=lambda: controller.show_frame(BooksPage),bg='deeppink',fg='white',font=('Open Sans',16,'bold'))
        b2.grid(row=2,column=0,padx=225,pady=25)  
        b3 = tk.Button(frame, text="Profile",
                            command=lambda: controller.show_frame(ProfilePage),bg='deeppink',fg='white',font=('Open Sans',16,'bold'))
        b3.grid(row=3,column=0,padx=225,pady=25)  
        b4 = tk.Button(frame, text="Borrow Book",
                            command=lambda: controller.show_frame(SignupPage),bg='deeppink',fg='white',font=('Open Sans',16,'bold'))
        b4.grid(row=4,column=0,padx=225,pady=25)  
        b1 = tk.Button(frame, text="Back to home",
                            command=lambda: controller.show_frame(LoginPage),bg='deeppink',fg='white',font=('Open Sans',16,'bold'))
        b1.grid(row=5,column=0,padx=225,pady=25)  


class BooksPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
            # Create the table frame and add it to the main window
        table_frame = tk.Frame(self)
        table_frame.pack(fill="both", expand=True)

        # Create the table header
        header = tk.Label(table_frame, text="Book List", font=("Arial", 16))
        header.pack()
        b1 = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(PageOne),bg='deeppink',fg='white',font=('Open Sans',16,'bold'))
        b1.pack()
        # Create a scrollbar and add it to the table frame
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side="right", fill="y")

        # Create a Treeview widget and add it to the table frame
        treeview = ttk.Treeview(table_frame, yscrollcommand=scrollbar.set, show="headings")
        treeview.pack(side="left", fill="both", expand=True)

        # Set the scrollbar to control the Treeview widget
        scrollbar.config(command=treeview.yview)



        values =book_listFN()

        # Add the column headings to the Treeview widget
        treeview["columns"] = ("col1", "col2", "col3","col4")
        treeview.column("col1", width=100)
        treeview.column("col2", width=100)
        treeview.column("col3", width=100)
        treeview.column("col4", width=100)
        treeview.heading("col1", text="Book code")
        treeview.heading("col2", text="Book name")
        treeview.heading("col3", text="Publisher")
        treeview.heading("col4", text="Author")

        # Add the values to the Treeview widget
        if values!=None:
            for i, value in enumerate(values):
                treeview.insert("", "end", text="i+1", values=value)


        def button_click():
        # Get the value from the text box
            value = text_box.get()
            # Insert the value into the label
            print(value)


        text_box = tk.Entry(self)
        text_box.pack()

        # Insert a default value into the text box
        text_box.insert(0, "Enter book code")

        # Create a button
        button = tk.Button(self, text="Add Book", command=button_click)
        button.pack()
 
class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
        self.backGroundImage = PhotoImage(file="bg3.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        self.title = Label(self, text="PROFILE", font=(
            'Microsoft Yehei UI Light', 16, 'bold'))
        self.title.place(x=300, y=60)

        self.nameLabel = Label(self, text="Name", font=(
            'Microsoft Yehei UI Light', 11))
        self.nameLabel.place(x=200, y=120)

        self.bookdetailsHead = Label(self, text="Date\t\tTitle\t\tAccession no.", font=(
            'Microsoft Yehei UI Light', 11))
        self.bookdetailsHead.place(x=200, y=170)
        b1 = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(PageOne),bg='deeppink',fg='white',font=('Open Sans',16,'bold'))
        b1.pack()
    """def Data(self):
        # self.name=Label(self,text=user.name,font=(
        # 'Microsoft Yehei UI Light', 11))
        # self.name.place(x=320, y=120)
        if(books.length == 0):  # using profileFn
            print("No books taken!")
        else:
            # estimate of no of books taken by a student-use for loop
            self.bookdetailsHead = Label(self, text="Date\t\tTitle\t\tAccession no.", font=(
                'Microsoft Yehei UI Light', 11))
            self.bookdetailsHead.place(x=200, y=170)"""
app = App()
app.mainloop()        
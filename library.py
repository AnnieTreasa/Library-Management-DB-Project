import tkinter as tk
from tkinter import *
from PIL import ImageTk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, SignupPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

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

        def signup_page():
            self.destroy
            import signup 

        

        heading=Label(self,text='USER LOGIN',font=('Microsoft Yehei UI Light',23,'bold'),bg='white',fg='firebrick2')
        heading.place(x=605,y=120)

        userEntry=Entry(self,width=25,font=('Microsoft Yehei UI Light',11,'bold'),bg='white',bd=0,fg='firebrick2')
        userEntry.place(x=580,y=200)
        userEntry.insert(0,'Username')

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

        loginButton =Button(self,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1',activeforeground='white',cursor='hand2',bd=0,width=19)
        loginButton.place(x=588,y=380)

        signupLabel = Label(self,text="Don't have an account?",font=('Open Sans',10),fg='firebrick1',bg='white')
        signupLabel.place(x=580,y=450)

        newaccountButton =Button(self,text='create new account',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activebackground='blue',activeforeground='white',cursor='hand2',bd=0,
        command=lambda: controller.show_frame(SignupPage))
        newaccountButton.place(x=727,y=450)

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
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
                            activebackground='firebrick1',activeforeground='white')
        signupButton.grid(row=13,column=0,padx=25,pady=(10,0),sticky='w')

        loginLabel = Label(self,text="Alredy have an account?",font=('Open Sans',10),fg='firebrick1',bg='white')
        loginLabel.place(x=580,y=500)

        loginButton =Button(self,text='Login',font=('Open Sans',9,'bold underline'),
        fg='blue',bg='white',activebackground='blue',activeforeground='white',cursor='hand2',bd=0,command= lambda: controller.show_frame(LoginPage))
        loginButton.place(x=730,y=500)

                            
       
app = App()
app.mainloop()        

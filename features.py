import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Anu@2001",
  database ="library"
)

db=mydb.cursor()


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




def registerFN(data):
    try:

        add_user_query="insert into user values(%s,%s,%s,%s,%s,%s)"
        adr = (data[0],data[1],data[2],data[3],data[4],data[5])
        db.execute(add_user_query,adr)
        mydb.commit()
        return True

    except mysql.connector.Error as err:
        print(err)
        return False



#registerFN(("20br13455","Anu","9999944678","ab@134","cse","2020"))

#a =loginFN("20br13455","ab@134")
#print(a)



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





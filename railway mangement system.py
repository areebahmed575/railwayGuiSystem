import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import *
import os

import mysql.connector as c


#main screen
master = Tk()
master.title("Railway system")

#functions

def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts= os.listdir()
    
    if name == "" or age == "" or gender == ""  or password == "":
        notif.config(fg="red",text="All fileds are required *")
        return

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="Account already exist")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green",text="Account has been created")

def register():
    #Var
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    

    #register screen
    register_screen = Toplevel(master)
    register_screen.title("Register")

    #labels
    Label(register_screen, text="Please enter your details below to register", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=("Calibri",12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=("Calibri",12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=("Calibri",12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=("Calibri",12)).grid(row=4,sticky=W)
    notif = Label(register_screen, font=("Calbiri",12))
    notif.grid(row=6,sticky=N,pady=10)                                      
                                         

    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0)

    #buttons
    Button(register_screen, text="register", command= finish_reg, font=("Calbiri",12)).grid(row=5,sticky=N,pady=10)

def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password  = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            #account dashoard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                #label
                Label(account_dashboard, text="Booking Dashboard", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome "+name, font=("Calibri",12)).grid(row=1,sticky=N,pady=5)

                #buttons
                Button(account_dashboard, text="book a ticket",font=("Calbiri",12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                Label(account_dashboard).grid(row=3,sticky=N,pady=10)
                return
                
                
            
                
            else:
                 login_notif.config(fg="red", text="Password incorrect!!")
                 return
    login_notif.config(fg="red", text="No accout found !!")

def update():
    code = t_code.get()
    name = t_name.get()
    city = t_city.get()
    destination = t_destination.get()
    ticketNo = t_ticketNo.get()
    members = t_members.get()
    con=c.connect(host="localhost",
              user="root",
              passwd="567575",
              database="dbmsproject")
    cursor=con.cursor()

    try:
       sql = "Update  ticket set name= %s,city= %s,destination= %s,ticketNo= %s,members= %s where code= %s "
       val = (name,city,destination,ticketNo,members,code)
       cursor.execute(sql, val)
       con.commit()
       lastid = cursor.lastrowid
       notif.config(fg="green",text="Registeration has been updated")
 
       t_code.delete(0, END)
       t_name.delete(0, END)
       t_city.delete(0, END)
       t_destination.delete(0, END)
       t_ticketNo.delete(0, END)
       t_members.delete(0, END)
       t_code.focus_set()
 
    except Exception as e:
 
       print(e)
       con.rollback()
       con.close()
    

def delete():
    code = t_code.get()
   
    con=c.connect(host="localhost",user="root",password="567575",database="dbmsproject")
    cursor=con.cursor()
 
    try:
       sql = "delete from ticket where code = %s"
       val = (code,)
       cursor.execute(sql, val)
       con.commit()
       lastid = cursor.lastrowid
       notif.config(fg="red",text= "Record Deleteeeee successfully...")

       t_code.delete(0, END)
       t_name.delete(0, END)
       t_city.delete(0, END)
       t_destination.delete(0, END)
       t_ticketNo.delete(0, END)
       t_members.delete(0, END)
       t_code.focus_set()
 
       
    except Exception as e:
         print(e)
         con.rollback()
         con.close()
     

   
def f_reg():
    code = t_code.get()
    name = t_name.get()
    city = t_city.get()
    destination = t_destination.get()
    ticketNo = t_ticketNo.get()
    members = t_members.get()
    con=c.connect(host="localhost",
              user="root",
              passwd="567575",
              database="dbmsProject")

    cursor=con.cursor()
    
    a_accounts= os.listdir()
    
    if code == "" or name == "" or city == ""  or destination == "" or ticketNo == "" or members == "" :
        notif.config(fg="red",text="All fileds are required *")
        return

    for code_check in a_accounts:
        if code == code_check:
            notif.config(fg="red",text="Registeration  already exist")
            return
        else:
           
            query="Insert into ticket values({},'{}','{}','{}',{},{})".format(code,name,city,destination,ticketNo,members)
            cursor.execute(query)
            con.commit()
            notif.config(fg="green",text="Registeration has been created")
            return






    
def personal_details():
    #Var
    global t_code
    global t_name
    global t_city
    global t_destination
    global t_ticketNo
    global t_members
    global notif
    
    t_code = StringVar()
    t_name = StringVar()
    t_city = StringVar()
    t_destination = StringVar()
    t_ticketNo = StringVar()
    t_members = StringVar()
    

    #register screen
    booking_screen = Toplevel(master)
    booking_screen.title("Registeration")

    #labels
    Label(booking_screen, text="Please enter your details ", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(booking_screen, text="Code:", font=("Calibri",12)).grid(row=1,sticky=W)
    Label(booking_screen, text="Name:", font=("Calibri",12)).grid(row=2,sticky=W)
    Label(booking_screen, text="City:", font=("Calibri",12)).grid(row=3,sticky=W)
    Label(booking_screen, text="Destination:", font=("Calibri",12)).grid(row=4,sticky=W)
    Label(booking_screen, text="TicketNo:", font=("Calibri",12)).grid(row=5,sticky=W)
    Label(booking_screen, text="Members:", font=("Calibri",12)).grid(row=6,sticky=W)
    notif = Label(booking_screen, font=("Calbiri",12))
    notif.grid(row=7,sticky=N,pady=10)                                      
                                         

    #Entries
    Entry(booking_screen,textvariable=t_code).grid(row=1,column=1)
    Entry(booking_screen,textvariable=t_name).grid(row=2,column=1)
    Entry(booking_screen,textvariable=t_city).grid(row=3,column=1)
    Entry(booking_screen,textvariable=t_destination).grid(row=4,column=1)
    Entry(booking_screen,textvariable=t_ticketNo).grid(row=5,column=1)
    Entry(booking_screen,textvariable=t_members).grid(row=6,column=1)

    #buttons
    Button(booking_screen, text="register",command = f_reg,font=("Calbiri",12)).grid(row=7,column=1,pady=10)
    Button(booking_screen, text="update",command = update,font=("Calbiri",12)).grid(row=8,column=1,pady=10)
    Button(booking_screen, text="delete",command=delete,font=("Calbiri",12)).grid(row=9,column=1,pady=10)
     
     
     
    
        
        

def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    #login Screen
    login_screen = Toplevel(master)
    login_screen.title("Login")

    #Labels
    Label(login_screen, text="Login to your account", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="UserName", font=("Calibri",12)).grid(row=1,sticky=W)
    Label(login_screen, text="Password", font=("Calibri",12)).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=("Calbiri",12))
    login_notif.grid(row=4,sticky=N)

    #Entry
    Entry(login_screen,textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen,textvariable=temp_login_password,show="*").grid(row=2,column=1,padx=5)

    #buttons
    Button(login_screen, text="Login", command= login_session, font=("Calbiri",12)).grid(row=3,sticky=W,pady=5,padx=5)     
    


    


#import image
img = PIL.Image.open('rail.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#labels
Label(master, text="Railway Management System", font=("Calibri",14)).grid(row=0,sticky=N,pady=10)
Label(master, image=img).grid(row=2,sticky=N,pady=15)


#register
Button(master, text="register", font=("Calibri",12),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="login", font=("Calibri",12),width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()

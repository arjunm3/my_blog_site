from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
#import pymysql
import sqlite3

def Acc_Register():
    #import sqlite3
    con=sqlite3.connect('myproject.db')
    cur=con.cursor()
    acc_num = acc_Info1.get()
    acc_name = acc_Info2.get()
    acc_type = acc_Info3.get()
    balance = acc_Info4.get()
    
    #status = status.lower()
    
    #insert_acc = "insert into "+acc_table+" values('"+acc_num+"','"+acc_name+"','"+acc_type+"','"+balance+"')"
    #print(insert_acc)
    try:
        
        cur.execute('insert into accounts values(?,?,?,?)',(acc_num,acc_name,acc_type,balance))
        con.commit()
        messagebox.showinfo('Success',"Account created successfully")
    except:
        
        messagebox.showinfo("Error","Can't add data into Database")
    
    #print(acc_num)
    #print(acc_name)
    #print(acc_type)
    #print(balance)


    root.destroy()
    
def add_acc(): 
    
    global acc_Info1,acc_Info2,acc_Info3,acc_Info4,Canvas1,con,cur,acc_table,root
    
    root = Tk()
    root.title("Banking portal")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.iconbitmap('myicon.ico')

    # Add your own database name and password here to reflect in the code

    #mypass = "Admin@123"
    #mydatabase="mydata"
    #import sqlite3
    #con=sqlite3.connect('myproject.db')
    #cur=con.cursor()



    
    #con = pymysql.connect(host="localhost",user="root",password="Admin@123",database="mydata")
    #cur = con.cursor()

    # Enter Account Names here
    #acc_table = "accounts" # Accounts Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#b8e994")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#c23616",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Create account", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Account No
    lb1 = Label(labelFrame,text="Account No : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    acc_Info1 = Entry(labelFrame)
    acc_Info1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Acc holder Name
    lb2 = Label(labelFrame,text="Acc holder Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    acc_Info2 = Entry(labelFrame)
    acc_Info2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Account Type
    lb3 = Label(labelFrame,text="Account Type : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    acc_Info3 = Entry(labelFrame)
    acc_Info3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Amount depositing
    lb4 = Label(labelFrame,text="Amount depositing : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    acc_Info4 = Entry(labelFrame)
    acc_Info4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=Acc_Register)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

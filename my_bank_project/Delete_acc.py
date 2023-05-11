from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
#import pymysql
import sqlite3

# Add your own database name and password here to reflect in the code
con=sqlite3.connect('myproject.db')
cur=con.cursor()

# Enter Table Names here
#issueTable = "books_issued" 
acc_Table = "accounts" #Accounts Table


def delete_acc():
    
    acc_no = acc_Info1.get()
    
    deleteSql = "delete from "+acc_Table+" where account_no = '"+acc_no+"'"
    #deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        #cur.execute(deleteIssue)
        #con.commit()
        messagebox.showinfo('Success',"Account closed Successfully")
    except:
        messagebox.showinfo("Please check the Account number")
    

    #print(bid)

    acc_Info1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global acc_Info1,Canvas1,con,cur,root
    
    root = Tk()
    root.title("Banking portal")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.iconbitmap('myicon.ico')

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Close an Account", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Account number to Delete
    lb2 = Label(labelFrame,text="Account Number : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    acc_Info1 = Entry(labelFrame)
    acc_Info1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=delete_acc)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

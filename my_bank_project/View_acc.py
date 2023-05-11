from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
#import pymysql
import sqlite3
con=sqlite3.connect('myproject.db')
cur=con.cursor()
# Add your own database name and password here to reflect in the code
#mypass = "root"
#mydatabase="db"

#con = pymysql.connect(host="localhost",user="root",password="Admin@123",database="mydata")
#cur = con.cursor()

# Enter Table Names here
accTable = "accounts" 
    
def View(): 
    
    root = Tk()
    root.title("Banking Portal")
    root.minsize(width=400,height=400)
    root.geometry("1920x1000")
    root.iconbitmap('myicon.ico')


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#c23616",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="ACCOUNT HOLDERS LIST", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg="#12a4d9")
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    style = ttk.Style()
    style.configure("Treeview",font=("times",14),rowheight=35)
    style.configure("Treeview.Heading",font=("times",15,"bold"))
    
    table = ttk.Treeview(labelFrame,columns=(0,1,2,3,4))
    table.column("0",anchor=CENTER)
    table.column("1",anchor=CENTER)
    table.column("2",anchor=CENTER)
    table.column("3",anchor=CENTER)
    table.column("4",anchor=CENTER)
    table.heading("0",text="S.NO")
    table.heading("1",text="Account Number")
    table.heading("2",text="Account Name")
    table.heading("3",text="Account Type")
    table.heading("4",text="Account Balance")
    table["show"]='headings'
    table.pack()



    
    #Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('acc_num','acc_name','acc_Type','acc_Balance'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    #Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    get_acc = "select * from "+accTable
    try:
        cur.execute(get_acc)
        con.commit()
        data=cur.fetchall()
        count=0
        for row in data:
            count+=1
            table.insert("",END,values=(count,row[0],row[1],row[2],row[3])    )
            #Label(labelFrame, text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
        y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

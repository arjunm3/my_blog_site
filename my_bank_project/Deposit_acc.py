from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
# Add your own database name and password here to reflect in the code


con=sqlite3.connect('myproject.db')
cur=con.cursor()

# Enter Table Names here
 
acc_Table = "accounts"
    
#List To store all Book IDs
all_acc = [] 

def deposit():
    
    global deposit_Btn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    acc_no = inf1.get()
    acc_no = int(acc_no)
    print(type(acc_no))
    deposit = inf2.get()
    deposit = int(deposit)

    #deposit_Btn.destroy()
    #labelFrame.destroy()
    #lb1.destroy()
    #inf1.destroy()
    #inf2.destroy()
    
    
    extract_acc = "select account_no from "+acc_Table
    print(extract_acc)
    try:
        cur.execute(extract_acc)
        con.commit()
        for i in cur:
            all_acc.append(i[0])
        print(all_acc)
        if acc_no in all_acc:
            acc_no = str(acc_no)
            check_bal = "select balance from "+acc_Table+" where account_no = '"+acc_no+"'"
            print(check_bal)
            cur.execute(check_bal)
            con.commit()
            for i in cur:
                temp=i[0]
            
            #print(temp)
            #print(type(temp))
            #temp = int(temp)
            temp = temp+deposit
            print(temp)
            temp = str(temp)
            new_bal="update accounts set balance = '"+temp+"' where account_no = '"+acc_no+"'"
            print(new_bal)
            #cur.execute('insert into accounts(balance) values(?)',(temp))
            cur.execute(new_bal)
            con.commit()
            messagebox.showinfo('Success',"Amount deposited successfully")

        else:
            messagebox.showinfo("Error","No accounts found for the given number !")
    except:
        messagebox.showinfo("Error","Can't fetch account details")
    deposit_Btn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    root.destroy
    all_acc.clear()
    
def deposit_amt(): 
    
    global deposit_Btn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Banking portal")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.iconbitmap('myicon.ico')
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Deposit Amount", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Account number
    lb1 = Label(labelFrame,text="Account number : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Amount to be deposited 
    lb2 = Label(labelFrame,text="Deposit Amount in ₹ : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #deposit_Btn
    deposit_Btn = Button(root,text="Deposit",bg='#d1ccc0', fg='black',command=deposit)
    deposit_Btn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


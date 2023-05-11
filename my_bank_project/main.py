from tkinter import *
from PIL import ImageTk,Image
#import pymysql
from tkinter import messagebox
from Add_acc import *
from Delete_acc import *
from View_acc import *
from Deposit_acc import *
from Withdraw_acc import *
from Qr_acc import *
#from ReturnBook import *
# Add your own database name and password here to reflect in the code
#mypass = "root"
#mydatabase="db"

#con = pymysql.connect(host="localhost",user="root",password="Admin@123",database="mydata")
#cur = con.cursor()
def main_func():
    
    root = Tk()
    root.title("Banking portal")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.iconbitmap('myicon.ico')

# Take n greater than 0.25 and less than 5
    same=True
    n=0.25

# Adding a background image
#background_image =Image.open("lib.jpg")
#[imageSizeWidth, imageSizeHeight] = background_image.size

#newImageSizeWidth = int(imageSizeWidth*n)
#if same:
#    newImageSizeHeight = int(imageSizeHeight*n) 
#else:
#    newImageSizeHeight = int(imageSizeHeight/n) 
    
#background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
#img = ImageTk.PhotoImage(background_image)

#Canvas1 = Canvas(root)

#Canvas1.create_image(300,340,image = img)      
#Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
#Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#c23616",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to Banking portal", bg='black', fg='white', font=('times',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="NEW ACCOUNT",bg='black', fg='white', command=add_acc)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="DEPOSIT AMOUNT",bg='black', fg='white', command=deposit_amt)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="WITHDRAW AMOUNT",bg='black', fg='white', command=withdraw_amt)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="GENERATE QR",bg='black', fg='white', command = generate_qr)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(root,text="ALL ACCOUNT DETAILS",bg='black', fg='white', command =View )
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

    btn6 = Button(root,text="CLOSE AN ACCOUNT",bg='black', fg='white', command = delete)
    btn6.place(relx=0.28,rely=0.9, relwidth=0.45,relheight=0.1)

    btn7 = Button(root,text="MODIFY AN ACCOUNT",bg='black', fg='white', command = deposit_amt)
    btn7.place(relx=0.28,rely=1.0, relwidth=0.45,relheight=0.1)

    root.mainloop()


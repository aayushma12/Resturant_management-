from tkinter import *
import tkinter.font as font
from PIL import Image,ImageTk


order_page= Tk()
order_page.geometry("1200x650")
order_page.title("Hotel Management System")
font1= font.Font(family="Georgia")
font2= font.Font(family="Georgia", size=8)
order_page.resizable(False,False)


# for Backgroung Image
bgimage=ImageTk.PhotoImage(file="order.jpg")
bglabel=Label(order_page, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Using pack for the main container
frame_pack = Frame(order_page, width=400, height=400)
frame_pack.place(relx=0.5, rely=0.5, anchor=CENTER)

welcome_label = Label(frame_pack,font=('Arial',20,'bold'), text="Welcome")
welcome_label.pack(padx=20, pady=20)
welcome_label = Label(frame_pack,font=('Arial',15,'bold'), text=" Select your option")
welcome_label.pack(padx=20, pady=20)

def addorder():
    order_page.destroy()
    import addorderpage
    
def vieworder():
    order_page.destroy()
    import vieworder
    


bt1=Button(frame_pack,text="Add Order",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=16,height=2,cursor='hand2', command= addorder)
bt1.pack(padx=20, pady=20)
bt2=Button(frame_pack,text="View Order",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=16,height=2,cursor='hand2', command= vieworder)
bt2.pack(padx=20, pady=20)

order_page.mainloop()

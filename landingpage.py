from tkinter import *
import tkinter.font as font
from PIL import Image,ImageTk


landing_page= Tk()
landing_page.geometry("1250x700")
landing_page.title("Hotel Management System")
# landing_page.configure(bg= "#ADD8E6")
font1= font.Font(family="Georgia")
font2= font.Font(family="Georgia", size=8)
landing_page.resizable(False,False)

#For background Image
bgimage=ImageTk.PhotoImage(file="landing.jpg")
bglabel=Label(landing_page, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
# Using pack for the main container
frame_pack = Frame(landing_page, width=400, height=400)
frame_pack.place(relx=0.5, rely=0.5, anchor=CENTER)

welcome_label = Label(frame_pack,font=('Arial',20,'bold'), text="Welcome")
welcome_label.pack(padx=20, pady=20)
welcome_label = Label(frame_pack,font=('Arial',15,'bold'), text=" Select your option")
welcome_label.pack(padx=20, pady=20)

def orderpage():
    landing_page.destroy()
    import Order_Page
def accountpage():
    landing_page.destroy()
    import Account
    
def kitchenpage():
    landing_page.destroy()
    import kitchen_page   
def staffpage():
    landing_page.destroy()
    import staffpage

bt1=Button(frame_pack,text="Order",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=16,height=2,cursor='hand2', command= orderpage)
bt1.pack(padx=20, pady=20)
bt2=Button(frame_pack,text="Kitchen",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=16,height=2,cursor='hand2', command= kitchenpage)
bt2.pack(padx=20, pady=20)
bt3=Button(frame_pack,text="Account",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=16,height=2,cursor='hand2', command= accountpage)
bt3.pack(padx=20, pady=20)
bt4=Button(frame_pack,text="Staff",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=16,height=2,cursor='hand2', command= staffpage)
bt4.pack(padx=20, pady=20)

landing_page.mainloop()

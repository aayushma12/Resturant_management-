
from tkinter import *
from PIL import Image,ImageTk


check_Order=Tk()
check_Order.title("Checked Order")
check_Order.geometry("1250x700")


    
# For background images 
bgimage=ImageTk.PhotoImage(file="check.jpg")
bglabel=Label(check_Order, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# For frame
bigbox=Label(check_Order,border=4,relief='ridge',height=40,width=140)
bigbox.place(x=150,y=60)

# To display Order
order_1=Label(bigbox,font=('Aapex',16),text=('Order 1 '))
order_1.place(x=60,y=200)

order_2=Label(bigbox,font=('Aapex',16),text=('Order 2 '))
order_2.place(x=60,y=250)

order_3=Label(bigbox,font=('Aapex',16),text=("Order 3"))
order_3.place(x=60,y=300)

# For Name_box
text1_box=Entry(bigbox,font=('Aapex',16),width=12)
text1_box.place(x=250,y=200)

# For Quantity_box
text2_box=Entry(bigbox,font=('Aapex',16),width=12)
text2_box.place(x=250,y=250)

# For price_box
text3_box=Entry(bigbox,font=('Aapex',16),width=12)
text3_box.place(x=250,y=300)

btn=Button(bigbox,font=('Aapex',16),relief='ridge',border=2,width=12,text=("Checked Button"),bg='light green')
btn.place(x=430,y=190)
#For Save button
order_completed_btn=Button(bigbox,font=('Aapex',16),relief='ridge',border=4,width=20,text=("Order Completed"),bg='light green')
order_completed_btn.place(x=400,y=560)
check_Order.mainloop()
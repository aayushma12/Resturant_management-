from tkinter import*
from PIL import Image,ImageTk


account_page=Tk()
account_page.title('WELCOME TO ACCOUNT')

# For background images 
bgimage=ImageTk.PhotoImage(file="im.jpg")
bglabel=Label(account_page, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# For frame 
Bigbox=LabelFrame(account_page,padx=150,pady=100)
Bigbox.pack(padx=300,pady=200)

# For box heading
box_heading=Label(Bigbox, text="View Detial Of Order", padx=20, pady=60)
box_heading.grid(row=0, column=0)

# For text_box
text_box=Entry(Bigbox,font=('Aapex',15),width=15)
text_box.place(x=1,y=1)

 

search=Label(Bigbox,font=('Aapex',16),text=("Search"))
search.place(x=150,y=1)

account_page.mainloop()
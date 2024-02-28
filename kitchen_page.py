from tkinter import*
from PIL import Image,ImageTk


kitchen_page=Tk()
kitchen_page.title('WELCOME TO KITCHEN')

# For background images 
bgimage=ImageTk.PhotoImage(file="beach.jpg")
bglabel=Label(kitchen_page, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# For frame 
frame=LabelFrame(kitchen_page,padx=50,pady=100)
frame.pack(padx=300,pady=200)

# For box heading
box_heading=Label(frame, text="View Order", padx=20, pady=10)
box_heading.grid(row=0, column=0)

kitchen_page.mainloop()
from tkinter import*
from PIL import Image,ImageTk


# For redirecting login button to login page 
def loginfunction():
    index_page.destroy() 
    import loginpage 


# For redirecting signup button to signup page 
def signupfunction():
    index_page.destroy()
    import signuppage


index_page=Tk()
index_page.title('WELCOME TO HOTEL MANAGEMENT SYSTEM')
index_page.geometry("1250x700")

# For background images 
bgimage=ImageTk.PhotoImage(file="hotel.jpg")
bglabel=Label(index_page, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)


# For frame 
frame=LabelFrame(index_page,padx=50,pady=100)
frame.pack(padx=10,pady=200)


# For box heading
box_heading=Label(frame, text="Login and Signup Here", padx=10, pady=20)
box_heading.grid(row=0, column=0)


# For login button
b=Button(frame,text=("Admin Login"),fg='Black',bg='sky blue', padx=10, command=loginfunction)
b.grid(row=2,column=0)


# For signup button
b1=Button(frame,text=("Admin Signup"),fg='black',bg='sky blue', command=signupfunction)
b1.grid(row=2,column=8)


index_page.mainloop()
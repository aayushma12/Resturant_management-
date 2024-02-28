from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

# For redirecting signup button to loginpage
def retrive_loginpg():
    signup_page.destroy()
    import loginpage

# Connect to mySql Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rosesareredstraw",
    database="hms_db"
)
cursor = db.cursor()

# Create table for Signup
cursor.execute("""CREATE TABLE IF NOT EXISTS user_login (id INT AUTO_INCREMENT PRIMARY KEY, 
               name VARCHAR(255),  
               username VARCHAR(255), 
               role VARCHAR(255), 
               password VARCHAR(255),
               email VARCHAR(255))""")

def signup():
    name=name_box.get()
    username=username_box.get()
    email=entry_email.get()
    role=role_box.get()
    password = password_box.get()
    cpassword = confirm_password_box.get()

    # Check if username already exists
    cursor.execute("SELECT * FROM user_login WHERE username=%s", (username,))
    if cursor.fetchone():
        messagebox.showerror("Error", "Username already exists.")
    elif password != cpassword:
        messagebox.showerror("Error", "Password and Confirm Password do not match.")
    else:
        # Insert new admin into the database
        cursor.execute("INSERT INTO user_login (name, username, role, password, email) VALUES (%s, %s, %s, %s, %s)", (name,username,role,password, email))
        db.commit()
        retrive_loginpg()
        messagebox.showinfo("Success", "Account created successfully.")



signup_page=Tk()
signup_page.title("Signup")

    
# For background images 
bgimage=ImageTk.PhotoImage(file="hotel2.jpg")
bglabel=Label(signup_page, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)



# Frames start
bigbox=Label(signup_page,border=4,relief='ridge',height=35,width=80)
bigbox.place(x=750,y=120)

# To display Name on screen
name=Label(bigbox,font=('Aapex',16),text=('Name :'))
name.place(x=50,y=80)

# For Name box
name_box=Entry(bigbox,font=('Aapex',16))
name_box.place(x=240,y=80)

# To display Username on screen
username=Label(bigbox,font=('Aapex',16),text=('Username :'))
username.place(x=50,y=140)

# For Username box
username_box=Entry(bigbox,font=('Aapex',16))
username_box.place(x=240,y=140)
    
# To display Role on screen
role=Label(bigbox,font=('Aapex',16),text=('Role :'))
role.place(x=50,y=200)

# For Role box
role_box=Entry(bigbox,font=('Aapex',16))
role_box.place(x=240,y=200)

# To display password on screen
password=Label(bigbox,font=('Aapex',16),text=('Password :'))
password.place(x=50,y=260)

# For Password box
password_box=Entry(bigbox,font=('Aapex',16))
password_box.place(x=240,y=260)

# To display Confirm password on screen
confirm_password=Label(bigbox,font=('Aapex',16),text=('Confirm Password :'))
confirm_password.place(x=50,y=320)

# For Confirm Password box
confirm_password_box=Entry(bigbox,font=('Aapex',16))
confirm_password_box.place(x=240,y=320)

# To display E-mail on screen
email=Label(bigbox,font=('Aapex',16),text=('E-mail :'))
email.place(x=50,y=380)

# For E-mail box
entry_email=Entry(bigbox,font=('Aapex',16))
entry_email.place(x=240,y=380)

# For Signup button
signupbtn=Button(bigbox,font=('Aapex',16),relief='ridge',border=4,width=6,text=("Signup"),bg='light green', command=signup)
signupbtn.place(x=220,y=450)

signup_page.mainloop()
from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

# For redirecting login button to landingpage
def landing():
    login_page.destroy()
    import landingpage

# Connect to mySql Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rosesareredstraw",
    database="resturant_ms"
)
cursor = db.cursor()


# Function to handle user login
def login():
    username = username_box.get()
    password = password_box.get()

    try:
            cursor.execute("SELECT * FROM user_login WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            if user:
                landing()
            else:
                messagebox.showerror("Error", "Invalid username or password")
    except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to login: {err}")
    finally:
            cursor.close()
            db.close()





login_page=Tk()
login_page.title("Login")
login_page.geometry("1250x700")

    
# For background images 
bgimage=ImageTk.PhotoImage(file="hotel1.jpg")
bglabel=Label(login_page, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)



# For frame
bigbox=Label(login_page,border=4,relief='ridge',height=35,width=60)
bigbox.place(x=850,y=150)

# To display Username on screen
username=Label(bigbox,font=('Aapex',16),text=('Username :'))
username.place(x=50,y=80)

# For Username box
username_box=Entry(bigbox,font=('Aapex',16))
username_box.place(x=160,y=80)

# To display Password on screen
password=Label(bigbox,font=('Aapex',16),text=('Password :'))
password.place(x=50,y=150)

# For Password box
password_box=Entry(bigbox,font=('Aapex',16))
password_box.place(x=160,y=150)

# For Login button
loginbtn=Button(bigbox,font=('Aapex',16),relief='ridge',border=4,width=6,text=("Login"),bg='light green', command=login)
loginbtn.place(x=150,y=260)


login_page.mainloop()


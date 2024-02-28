from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk


# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rosesareredstraw",
    database="hms_db"
)    

# Create a cursor object to interact with the database
mycursor = db.cursor()

# Create 'admin' table if not exists
mycursor.execute('''CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(20) NOT NULL)''')


mycursor.execute("""CREATE TABLE IF NOT EXISTS orders (id INT AUTO_INCREMENT PRIMARY KEY, 
               customer_id INT,
               item_name VARCHAR(255) NOT NULL,
               quantity INT NOT NULL,
               price DECIMAL(10, 2) NOT NULL,
               FOREIGN KEY (customer_id) REFERENCES customers(id))""")



def addBox():
    
    frame = Frame(New_Order)
    frame.pack()
    Label(frame, text='Item Name').grid(row=0, column=0)

    ent1 = Entry(frame)
    ent1.grid(row=1, column=0)

    Label(frame, text='Quantity').grid(row=0, column=1)

    ent2 = Entry(frame)
    ent2.grid(row=1, column=1)
    
    Label(frame, text='Price').grid(row=0, column=2)
    ent3 = Entry(frame)
    ent3.grid(row=1, column=2)
    
    all_entries.append( (ent1, ent2, ent3) )
    

def save_order():
    # Retrieve data from Tkinter entries
    name = name_box.get()
    contact = contact_box.get()
   

    # Insert customer data into the database
    mycursor.execute("INSERT INTO customers (name, contact) VALUES (%s, %s)", (name, contact))
    db.commit()

    # Retrieve the customer ID
    customer_id = mycursor.lastrowid

    # Insert order details into the database
    for entry_set in all_entries:
        item_name, quantity, price = [entry.get() for entry in entry_set]
        mycursor.execute("INSERT INTO orders (customer_id, item_name, quantity, price) VALUES (%s, %s, %s, %s)",
                         (customer_id, item_name, quantity, price))
        db.commit()

    messagebox.showinfo("Success", "Order saved successfully!")
all_entries = []
New_Order=Tk()
New_Order.title("New_Order")


# For background images 
bgimage=ImageTk.PhotoImage(file="tower.jpg")
bglabel=Label(New_Order, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)


# To display Name on screen
name=Label(New_Order,font=('Aapex',16),text=('Name :'))
name.pack()

# For Name box
name_box=Entry(New_Order,font=('Aapex',16))
name_box.pack()


# To display Contact on screen
contact=Label(New_Order,font=('Aapex',16),text=('Contact :'))
contact.pack()

# For Contact box_box
contact_box=Entry(New_Order,font=('Aapex',16))
contact_box.pack()



# For Login button
add_item_btn=Button(New_Order,font=('Aapex',16),relief='ridge',border=4,width=10,text=("Add Item"),bg='light green', command=addBox)
add_item_btn.place(x=40,y=560)

#For Save button
save_btn=Button(New_Order,font=('Aapex',16),relief='ridge',border=4,width=10,text=("Save"),bg='light green', command=save_order)
save_btn.place(x=550,y=560)

New_Order.mainloop()

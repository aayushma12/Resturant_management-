# import tkinter as tk

# root = tk.Tk()
# root.title("check button")

# # Create the main frame
# main_frame = tk.Frame(root)
# main_frame.pack(padx=500, pady=200)

# # Create text labels
# text1_label = tk.Label(main_frame, text="Order 1:")
# text1_label.grid(row=0, column=0)
# text1_entry = tk.Entry(main_frame)
# text1_entry.grid(row=0, column=1)

# text2_label = tk.Label(main_frame, text="Order 2:")
# text2_label.grid(row=1, column=0)
# text2_entry = tk.Entry(main_frame)
# text2_entry.grid(row=1, column=1)

# #for order button
# orderbtn1=tk.Button(main_frame)
# orderbtn1.place(x=167,y=1 , bg='yellow')


# # Create button
# button = tk.Button(main_frame, text="Order Completed")
# button.grid(row=2, column=0, columnspan=2, pady=10)

# root.mainloop()

# from tkinter import *
# Check_Order=Tk()
# Check_Order.title("Checked Order")

    
# For background images 
# bgimage=ImageTk.PhotoImage(file="hotel1.jpg")
# bglabel=Label(login_page, image=bgimage)
# bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# For frame
# bigbox=Label(Check_Order,border=4,relief='ridge',height=40,width=140)
# bigbox.place(x=150,y=60)

# # To display Order
# order_1=Label(bigbox,font=('Aapex',16),text=('Order 1 '))
# order_1.place(x=60,y=200)

# order_2=Label(bigbox,font=('Aapex',16),text=('Order 2 '))
# order_2.place(x=60,y=250)

# order_3=Label(bigbox,font=('Aapex',16),text=("Order 3"))
# order_3.place(x=60,y=300)

# # For Name_box
# text1_box=Entry(bigbox,font=('Aapex',16),width=12)
# text1_box.place(x=250,y=200)

# # For Quantity_box
# text2_box=Entry(bigbox,font=('Aapex',16),width=12)
# text2_box.place(x=250,y=250)

# # For price_box
# text3_box=Entry(bigbox,font=('Aapex',16),width=12)
# text3_box.place(x=250,y=300)

# btn=Button(bigbox,font=('Aapex',16),relief='ridge',border=2,width=12,text=("Checked Button"),bg='light green')
# btn.place(x=430,y=190)
# #For Save button
# order_completed_btn=Button(bigbox,font=('Aapex',16),relief='ridge',border=4,width=20,text=("Order Completed"),bg='light green')
# order_completed_btn.place(x=400,y=560)
# Check_Order.mainloop()



from tkinter import *
import mysql.connector
from tkinter import messagebox

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
# For frame


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
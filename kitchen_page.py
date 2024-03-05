import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import Image,ImageTk

def fetch_customer_and_order_data():
    # Clear previous data in the treeview
    for record in tree.get_children():
        tree.delete(record)

    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rosesareredstraw",
            database="resturant_ms"
        )
        cursor = connection.cursor()

        # Execute SQL query to fetch unique customer details
        query = """
            SELECT DISTINCT customers.id, customers.name, customers.contact
            FROM customers
            LEFT JOIN orders ON customers.id = orders.customer_id
        """
        cursor.execute(query)
        customer_records = cursor.fetchall()

        # Loop through each customer and fetch associated order details
        for customer_record in customer_records:
            customer_id, customer_name, customer_contact = customer_record

            # Insert customer details into the treeview
            tree.insert('', 'end', values=(customer_id, customer_name, customer_contact, '', '', '', ''))

            # Execute SQL query to fetch orders for the current customer
            order_query = f"""
                SELECT orders.item_name, orders.quantity, orders.price
                FROM orders
                WHERE orders.customer_id = {customer_id}
            """
            cursor.execute(order_query)
            order_records = cursor.fetchall()

            # Insert order details into the treeview
            for order_record in order_records:
                tree.insert('', 'end', values=('', '', '', *order_record))

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Tkinter setup

root = tk.Tk()
root.title("Customer and Order Data Fetcher")
root.geometry("1250x700")

#For gackground Image
bgimage=ImageTk.PhotoImage(file="sunset.jpg")
bglabel=tk.Label(root, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Treeview for displaying data
columns = ('ID', 'Name', 'Contact', 'Item Name', 'Quantity', 'Price')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=10)

# Button to fetch data
fetch_button = tk.Button(root, text="Fetch Customer and Order Data", command=fetch_customer_and_order_data)
fetch_button.pack(pady=10)


# Run the Tkinter main loop
root.mainloop()

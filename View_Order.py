import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


def search_by_phone():
    # Clear previous data in the treeview
    for record in tree.get_children():
        tree.delete(record)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rosesareredstraw",
            database="resturant_ms"
        )
        cursor = connection.cursor()

        # Get the phone number from the entry widget
        phone_number = phone_entry.get()

        # Execute SQL query to fetch combined data from customers and orders tables
        query = f"""
            SELECT customers.name, customers.contact
            FROM customers
            WHERE customers.contact = '{phone_number}'
        """
        cursor.execute(query)
        customer_details = cursor.fetchone()

        if customer_details:
            # Insert customer details into the treeview
            tree.insert('', 'end', values=customer_details)
            # tree.insert('', 'end', values=('', '', '', customer_details))


            # Execute another query to fetch order details
            query = f"""
                SELECT orders.item_name, orders.quantity, orders.price
                FROM orders
                WHERE orders.customer_id = (
                    SELECT id FROM customers WHERE contact = '{phone_number}'
                )
            """
            cursor.execute(query)
            order_details = cursor.fetchall()

            # Insert order details into the treeview
            for order_detail in order_details:
                tree.insert('', 'end', values=['', ''] + list(order_detail))
                # tree.insert('', 'end', values=('', '', '', order_details))
        else:
            print("Customer not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def delete_selected_item():
    # Get the selected item from the Treeview
    selected_item = tree.selection()

    if selected_item:
        # Extract customer details from the selected item
        customer_name, customer_contact, *_ = tree.item(selected_item, 'values')

        try:
            # Connect to MySQL database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="rosesareredstraw",
                database="resturant_ms"
            )
            cursor = connection.cursor()

            # Delete the corresponding records from the 'orders' table
            cursor.execute("""
                DELETE FROM orders
                WHERE customer_id = (
                    SELECT id FROM customers WHERE name = %s AND contact = %s
                )
            """, (customer_name, customer_contact))

            # Delete the selected item from the 'customers' table
            cursor.execute("""
                DELETE FROM customers
                WHERE name = %s AND contact = %s
            """, (customer_name, customer_contact))

            # Commit the changes to the database
            connection.commit()

            # Delete the selected item from the Treeview
            tree.delete(selected_item)

            messagebox.showinfo("Success", "Record deleted successfully!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", "Failed to delete record. Check the console for details.")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Tkinter setup
root = tk.Tk()
root.title("Search by Phone Number")
root.geometry("1250x700")

# For background images 
bgimage=ImageTk.PhotoImage(file="winter.jpg")
bglabel=tk.Label(root, image=bgimage)
bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Entry widget for entering the phone number
phone_label = tk.Label(root, text="Enter Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack(pady=5)

# Treeview for displaying data
columns = ('Customer Name', 'Contact', 'Item Name', 'Quantity', 'Price')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=10)

# Button to search and display data
search_button = tk.Button(root, text="Search by Phone Number", command=search_by_phone)
search_button.pack(pady=10)

delete_button = tk.Button(root, text="delete", command=delete_selected_item)
delete_button.pack(pady=10)
# Run the Tkinter main loop
root.mainloop()

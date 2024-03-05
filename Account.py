import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image,ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
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

            total_price = 0  # Variable to store the total price

            # Insert order details into the treeview
            for order_detail in order_details:
                tree.insert('', 'end', values=['', ''] + list(order_detail))
                total_price += order_detail[2]  # Add the price to the total

            # Insert total price row
            tree.insert('', 'end', values=('', '','', 'Total Price:', total_price))
        else:
            print("Customer not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def generate_and_save_pdf(customer_name, customer_contact, order_details, total_price, pdf_filename):
    try:
        pdf_canvas = canvas.Canvas(pdf_filename, pagesize=letter)
        pdf_canvas.drawString(72, 600, f'Bill for {customer_name}')
        pdf_canvas.drawString(72, 620, f'Contact: {customer_contact}')

        # Insert headings into the PDF
        pdf_canvas.drawString(72, 580, 'Item Name')
        pdf_canvas.drawString(200, 580, 'Quantity')
        pdf_canvas.drawString(350, 580, 'Price')

        # Insert order details into the PDF
        y_position = 560
        for order_detail in order_details:
            pdf_canvas.drawString(72, y_position, f'{order_detail["item_name"]}')
            pdf_canvas.drawString(200, y_position, f'{order_detail["quantity"]}')
            pdf_canvas.drawString(350, y_position, f'RS. {order_detail["price"]}')
            y_position -= 15

        # Draw a line to separate order details from total price
        pdf_canvas.line(72, y_position, 550, y_position)

        # Insert total price into the PDF below the line
        pdf_canvas.drawString(300, y_position - 20, f'Total Price: Rs. {total_price}')

        pdf_canvas.save()

        print(f'Bill generated and saved at: {pdf_filename}')
        messagebox.showinfo("Success", "Bill generated and saved successfully!")

    except Exception as e:
        print(f"Error generating PDF: {e}")
        messagebox.showerror("Error", "Failed to generate and save the bill.")




def save_bill():
    # Get customer details from the Treeview
    customer_name = tree.item(tree.get_children()[0], 'values')[0]  # Fix: Index should be 0
    customer_contact = tree.item(tree.get_children()[0], 'values')[1]  # Fix: Index should be 1

    # Get order details from the Treeview
    order_details = []
    for item in tree.get_children():
        values = tree.item(item, 'values')
        if values and len(values) >= 5:  # Fix: Changed to 5 since there are 5 columns in the Treeview
            order_details.append({
                'item_name': values[2],  
                'quantity': values[3],   
                'price': values[4]      
            })

    # Get total price from the Treeview
    try:
        total_price = float(tree.item(tree.get_children()[-1], 'values')[-1])
    except (ValueError, IndexError):
        messagebox.showerror("Error", "Failed to generate bill. Total price not available.")
        return

    # Generate and save the bill
     # Generate and save the bill
    output_folder = r'D:\Hotel Management System\Bills'
    pdf_filename = os.path.join(output_folder, f'Bill_{customer_name}.pdf')

    generate_and_save_pdf(customer_name, customer_contact, order_details, total_price, pdf_filename)
    
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
search_button = tk.Button(root, text="Search", command=search_by_phone)
search_button.pack(pady=10)
bill_button = tk.Button(root, text="Save Bill", command=save_bill)
bill_button.pack(pady=10)
delete_button = tk.Button(root, text="Finish", command=delete_selected_item)
delete_button.pack(pady=10)
# Run the Tkinter main loop
root.mainloop()

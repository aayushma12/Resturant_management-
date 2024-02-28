import tkinter as tk
from tkinter import PhotoImage

def on_search_click():
    search_text = search_entry.get()
    print(f"Searching for: {search_text}")

def on_button1_click():
    print("Button 1 clicked!")

def on_button2_click():
    print("Button 2 clicked!")

root = tk.Tk()
root.title("Frame Example")

# Create the main frame
main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Create search box
search_label = tk.Label(main_frame, text="Search:")
search_label.grid(row=0, column=0)
search_entry = tk.Entry(main_frame)
search_entry.grid(row=0, column=1)
search_button = tk.Button(main_frame, text="Search", command=on_search_click)
search_button.grid(row=0, column=2)

# Create small frame inside main frame
small_frame = tk.Frame(main_frame, bd=1, relief=tk.GROOVE)
small_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky="ew")

# Create buttons inside the small frame
button1 = tk.Button(small_frame, text="Edit", command=on_button1_click)
button1.pack(side=tk.LEFT, padx=5, pady=5)
button2 = tk.Button(small_frame, text="Update", command=on_button2_click)
button2.pack(side=tk.LEFT, padx=5, pady=5)

# Load and display a background image in the small frame
bg_image = PhotoImage("tower.jpg")
bg_label = tk.Label(small_frame, image=bg_image)
bg_label.pack(fill=tk.BOTH, expand=True)

root.mainloop()

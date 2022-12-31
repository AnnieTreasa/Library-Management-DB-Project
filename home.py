import tkinter as tk
import tkinter.ttk as ttk
from features import book_listFN


# Create the main window
window = tk.Tk()
window.geometry("500x500+100+200")
window.title("Library")

# Create the table frame and add it to the main window
table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True)

# Create the table header
header = tk.Label(table_frame, text="Book List", font=("Arial", 16))
header.pack()

# Create a scrollbar and add it to the table frame
scrollbar = tk.Scrollbar(table_frame)
scrollbar.pack(side="right", fill="y")

# Create a Treeview widget and add it to the table frame
treeview = ttk.Treeview(table_frame, yscrollcommand=scrollbar.set, show="headings")
treeview.pack(side="left", fill="both", expand=True)

# Set the scrollbar to control the Treeview widget
scrollbar.config(command=treeview.yview)



values =book_listFN()

# Add the column headings to the Treeview widget
treeview["columns"] = ("col1", "col2", "col3","col4")
treeview.column("col1", width=100)
treeview.column("col2", width=100)
treeview.column("col3", width=100)
treeview.column("col4", width=100)
treeview.heading("col1", text="Book code")
treeview.heading("col2", text="Book name")
treeview.heading("col3", text="Publisher")
treeview.heading("col4", text="Author")

# Add the values to the Treeview widget
if values!=None:
    for i, value in enumerate(values):
        treeview.insert("", "end", text="i+1", values=value)


def button_click():
  # Get the value from the text box
  value = text_box.get()
  # Insert the value into the label
  print(value)


text_box = tk.Entry(window)
text_box.pack()

# Insert a default value into the text box
text_box.insert(0, "Enter book code")

# Create a button
button = tk.Button(window, text="Add Book", command=button_click)
button.pack()
# Run the Tkinter event loop
window.mainloop()
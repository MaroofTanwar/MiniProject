# 1. Import the required libraries:
from tkinter import *
import tkinter.messagebox as messagebox

# 2. Create a main window and set its properties:
root = Tk()
root.title("Contact Management System")

# 3. Create a function to add a new contact:
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()

    if name == "" or phone == "":
        messagebox.showwarning("Incomplete information", "Please enter both name and phone number.")
    else:
        contact_list.insert(END, name + " - " + phone)
        entry_name.delete(0, END)
        entry_phone.delete(0, END)

# 4. Create a function to delete a contact:
def delete_contact():
    try:
        selected_contact = contact_list.curselection()
        contact_list.delete(selected_contact)
    except:
        messagebox.showwarning("No contact selected", "Please select a contact to delete.")

# 5. Create the GUI elements:
label_name = Label(root, text="Name:")
label_name.grid()
entry_name = Entry(root)
entry_name.grid()

label_phone = Label(root, text="Phone:")
label_phone.grid()
entry_phone = Entry(root)
entry_phone.grid()

button_add = Button(root, text="Add Contact", command=add_contact)
button_add.grid()

button_delete = Button(root, text="Delete Contact", command=delete_contact)
button_delete.grid()

contact_list = Listbox(root)
contact_list.grid()

# 6. Start the main loop:
root.mainloop()
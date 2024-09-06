import tkinter as tk
from tkinter import messagebox, ttk

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if name == "" or phone == "" or email == "":
        messagebox.showwarning("Input Error", "All fields are required!")
    elif name in contacts:
        messagebox.showerror("Duplicate Entry", "Contact already exists!")
    else:
        contacts[name] = {'Phone': phone, 'Email': email}
        messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
        clear_fields()
        show_contacts()

# Function to update an existing contact
def update_contact():
    selected_item = contact_list.selection()
    if selected_item:
        old_name = contact_list.item(selected_item)['values'][0]  # Get the old name
        new_name = entry_name.get().strip()
        phone = entry_phone.get().strip()
        email = entry_email.get().strip()

        if new_name == "" or phone == "" or email == "":
            messagebox.showwarning("Input Error", "All fields are required!")
        else:
            if old_name in contacts:
                del contacts[old_name]  # Remove the old entry

            contacts[new_name] = {'Phone': phone, 'Email': email}
            messagebox.showinfo("Success", f"Contact '{new_name}' updated successfully!")
            clear_fields()
            show_contacts()
    else:
        messagebox.showerror("Not Found", "Please select a contact to update!")

# Function to delete a contact
def delete_contact():
    selected_item = contact_list.selection()
    if selected_item:
        name = contact_list.item(selected_item)['values'][0]
        if name in contacts:
            del contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
            clear_fields()
            show_contacts()
        else:
            messagebox.showerror("Error", "Contact not found!")
    else:
        messagebox.showerror("Not Found", "Please select a contact to delete!")

# Function to display all contacts
def show_contacts():
    contact_list.delete(*contact_list.get_children())  # Clear the list
    for name, details in contacts.items():
        contact_list.insert("", tk.END, values=(name, details['Phone'], details['Email']))

# Function to clear input fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Function to show the selected contact data in entry fields
def select_contact(event):
    selected_item = contact_list.selection()
    if selected_item:
        name = contact_list.item(selected_item)['values'][0]
        phone = contacts[name]['Phone']
        email = contacts[name]['Email']

        # Show selected contact details in entry fields
        clear_fields()
        entry_name.insert(0, name)
        entry_phone.insert(0, phone)
        entry_email.insert(0, email)

# Create the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x400")

# Configure grid for responsiveness
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Name Entry
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

# Phone Entry
tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

# Email Entry
tk.Label(root, text="Email:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

# Buttons for CRUD operations
btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

btn_update = tk.Button(root, text="Update Contact", command=update_contact)
btn_update.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

# Table to display contacts
columns = ('Name', 'Phone', 'Email')
contact_list = ttk.Treeview(root, columns=columns, show='headings')
contact_list.heading('Name', text='Name')
contact_list.heading('Phone', text='Phone')
contact_list.heading('Email', text='Email')
contact_list.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

# Bind the treeview selection event to the select_contact function
contact_list.bind('<<TreeviewSelect>>', select_contact)

# Make the table responsive
root.grid_rowconfigure(4, weight=3)

# Start the GUI main loop
root.mainloop()

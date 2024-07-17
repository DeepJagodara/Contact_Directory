import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ContactDirectory:
    def __init__(self, root):   # Constructor method to initialize the ContactDirectory class
        self.root = root
        self.contacts = {}  #Dictionary store value in key:value pairs
        self.load_contacts()    # method Load contacts from file when the program starts

        self.root.title("Contact Directory")
        self.root.geometry("400x340")
        self.title_label = tk.Label(self.root, text="Contact Directory", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack()

        # Buttons for different functionalities
        self.add_button = tk.Button(self.menu_frame, text="Add Contact", command=self.add_person, width=15)
        self.add_button.grid(row=0, column=0, pady=5)

        self.update_button = tk.Button(self.menu_frame, text="Update Contact", command=self.update_person, width=15)
        self.update_button.grid(row=1, column=0, pady=5)

        self.search_button = tk.Button(self.menu_frame, text="Search Contact", command=self.search_person, width=15)
        self.search_button.grid(row=2, column=0, pady=5)

        self.remove_button = tk.Button(self.menu_frame, text="Remove Contact", command=self.remove_person, width=15)
        self.remove_button.grid(row=3, column=0, pady=5)
        
        self.remove_button = tk.Button(self.menu_frame, text="show all contacts", command=self.show_all_contacts, width=15)
        self.remove_button.grid(row=4, column=0, pady=5)

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=self.save_and_exit, width=15)
        self.exit_button.grid(row=5, column=0, pady=5)

        self.exit_button = tk.Button(self.menu_frame, text="Enter", command=self.enter, width=15)
        self.exit_button.grid(row=6, column=0, pady=5)

    def add_person(self):
        # Function to add a new person to the contact directory
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Person")
        name_label = tk.Label(add_window, text="Enter Person's Name: ")
        name_label.grid(row=0, column=0,pady=5)
        self.name_entry = tk.Entry(add_window)
        self.name_entry.grid(row=0, column=1)

        number_label = tk.Label(add_window, text="Enter Person's Contact Number: ")
        number_label.grid(row=1, column=0)
        self.number_entry = tk.Entry(add_window)
        self.number_entry.grid(row=1, column=1,pady=5)

        email_label = tk.Label(add_window, text="Enter Person's Email: ")
        email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(add_window)
        self.email_entry.grid(row=2, column=1,pady=5)

        add_button = tk.Button(add_window, text="Add", command=self.add_person_action)
        add_button.grid(row=3, columnspan=2,pady=5)

    def add_person_action(self):
        # Function to perform the action of adding a person
        name = self.name_entry.get()
        number = self.number_entry.get()
        email = self.email_entry.get()
    
        if self.check_existing_name(name):
            messagebox.showerror("Error", f"Contact with name '{name}' already exists.")
        elif len(number) != 10 or not number.isdigit():
            messagebox.showerror("Error", "Contact Number Must Be 10 Digits Long.")
        else:
            self.contacts[name] = {'number': number, 'email': email}
            messagebox.showinfo("Success", "Contact Added Successfully.")
            self.save_contacts()
            self.name_entry.delete(0, tk.END)
            self.number_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)

    # Similar methods for updating, searching, removing persons, and displaying the directory

    def check_existing_name(self, name):
        with open("contacts.txt", "r") as file:
            for line in file:
                data = line.strip().split(":")
                if data[0] == name:
                    return True
        return False


    def update_person(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Person")

        name_label = tk.Label(update_window, text="Enter Person's Name To Update: ")
        name_label.grid(row=0, column=0,pady=5)
        self.name_entry = tk.Entry(update_window)
        self.name_entry.grid(row=0, column=1,pady=5)

        update_button = tk.Button(update_window, text="Update", command=self.update_person_action)
        update_button.grid(row=1, columnspan=2,pady=5)

    def update_person_action(self):
        name = self.name_entry.get()
        if name in self.contacts:
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Contact")

            new_name_label = tk.Label(update_window, text="Enter New Name (Or Leave Empty To Keep Old Name): ")
            new_name_label.grid(row=0, column=0)
            self.new_name_entry = tk.Entry(update_window)
            self.new_name_entry.grid(row=0, column=1,pady=5)

            new_number_label = tk.Label(update_window, text="Enter New Contact Number (Or Leave Empty To Keep Old Number): ")
            new_number_label.grid(row=1, column=0,pady=5)
            self.new_number_entry = tk.Entry(update_window)
            self.new_number_entry.grid(row=1, column=1,pady=5)

            new_email_label = tk.Label(update_window, text="Enter New Email (Or Leave Empty To Keep Old Email): ")
            new_email_label.grid(row=2, column=0,pady=5)
            self.new_email_entry = tk.Entry(update_window)
            self.new_email_entry.grid(row=2, column=1,pady=5)

            update_button = tk.Button(update_window, text="Update", command=self.update_contact)
            update_button.grid(row=3, columnspan=2,pady=5)
        else:
            messagebox.showerror("Error", "Person not found.")

    def update_contact(self):
        old_name = self.name_entry.get()
        new_name = self.new_name_entry.get()
        new_number = self.new_number_entry.get()
        new_email = self.new_email_entry.get()

        if new_name or new_number or new_email:
            if new_name:
                self.contacts[new_name] = self.contacts.pop(old_name)
            if new_number:
                if len(new_number) != 10 or not new_number.isdigit():
                    messagebox.showerror("Error", "Contact Number Must Be 10 Digits Long.")
                else:
                    self.contacts[new_name]['number'] = new_number
            if new_email:
                self.contacts[new_name]['email'] = new_email
            messagebox.showinfo("Success", "Contact updated successfully.")
            self.save_contacts()
        else:
            messagebox.showinfo("Info", "No changes made.")

    def search_person(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search contact")

        name_label = tk.Label(search_window, text="Enter Person's Name To Search: ")
        name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(search_window)
        self.name_entry.grid(row=0, column=1)

        search_button = tk.Button(search_window, text="Search", command=self.search_person_action)
        search_button.grid(row=1, columnspan=2,pady=5)

    def search_person_action(self):
        name = self.name_entry.get()
        if name in self.contacts:
            contact_info = f"Name: {name}\nContact Number: {self.contacts[name]['number']}\nEmail: {self.contacts[name]['email']}"
            messagebox.showinfo("Info", contact_info)
        else:
            messagebox.showinfo("Info", "Contact Not Found...")

    def remove_person(self):
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Person")

        name_label = tk.Label(remove_window, text="Enter Person's Name To Remove: ")
        name_label.grid(row=0, column=0,pady=5)
        self.name_entry = tk.Entry(remove_window)
        self.name_entry.grid(row=0, column=1,pady=5)

        remove_button = tk.Button(remove_window, text="Remove", command=self.remove_person_action)
        remove_button.grid(row=1, columnspan=2,pady=5)

    def remove_person_action(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Info", "Contact Removed Successfully.")
            self.save_contacts()
        else:
            messagebox.showerror("Error", "Contact Not Found.")

    def show_all_contacts(self):
        all_contacts_window = tk.Toplevel(self.root)
        all_contacts_window.title("All Contacts")

        tree = ttk.Treeview(all_contacts_window, columns=("Name", "Contact Number", "Email"), show="headings")
        tree.heading("Name", text="Name")
        tree.heading("Contact Number", text="Contact Number")
        tree.heading("Email", text="Email")
        tree.pack(expand=True, fill=tk.BOTH)

        for name, contact_info in self.contacts.items():
            tree.insert("", "end", values=(name, contact_info['number'], contact_info['email']))

        if not self.contacts:
            tree.insert("", "end", values=("No contacts available", "", ""))

        scrollbar = ttk.Scrollbar(all_contacts_window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

    def load_contacts(self):
        # Function to load contacts from a file
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    data = line.strip().split(":")
                    if len(data) == 3:
                        name, number, email = data
                        self.contacts[name] = {'number': number, 'email': email}
                    elif len(data) == 2:
                        name, number = data
                        self.contacts[name] = {'number': number, 'email': ''}
        except FileNotFoundError:
            pass



    def save_contacts(self):
        # Function to save contacts to a file
        with open("contacts.txt", "w") as file:
            for name, contact in self.contacts.items():
                file.write(f"{name}:{contact['number']}:{contact['email']}\n")

    def save_and_exit(self):
        # Function to save contacts and exit the application
        self.save_contacts()
        self.root.destroy()

    def enter(self):
        # Function to save contacts and exit the application
        self.save_contacts()
        self.root.destroy()

root = tk.Tk()  # Create a Tkinter root window
app = ContactDirectory(root)    # Create an object of ContactDirectory class
root.mainloop() # Start the Tkinter event loop
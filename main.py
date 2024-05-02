import pickle
import tkinter as tk
from tkinter import ttk

class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, dob, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details

class Event:
    def __init__(self, event_id, name, date, location, description):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.description = description

class Client:
    def __init__(self, client_id, name, email, phone):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

class Supplier:
    def __init__(self, supplier_id, name, products, contact_person, email, phone):
        self.supplier_id = supplier_id
        self.name = name
        self.products = products
        self.contact_person = contact_person
        self.email = email
        self.phone = phone

class Guest:
    def __init__(self, guest_id, name, email, phone):
        self.guest_id = guest_id
        self.name = name
        self.email = email
        self.phone = phone

class Venue:
    def __init__(self, venue_id, name, location, capacity, contact_person, email, phone):
        self.venue_id = venue_id
        self.name = name
        self.location = location
        self.capacity = capacity
        self.contact_person = contact_person
        self.email = email
        self.phone = phone


# Example function to save employees data
def save_employees_data(employees):
    with open('employees.pkl', 'wb') as f:
        pickle.dump(employees, f)

# Example function to load employees data
def load_employees_data():
    try:
        with open('employees.pkl', 'rb') as f:
            employees = pickle.load(f)
            return employees
    except FileNotFoundError:
        return []

class EventManagementGUI:
    def __init__(self, master):
        self.master = master
        master.title("Event Management System")
        master.geometry("500x350")
        master.config(bg="#f0f0f0")

        # Title Label
        self.label = tk.Label(master, text="Welcome to Event Management System", font=("Arial", 18), bg="#f0f0f0")
        self.label.pack(pady=20)

        # Button Style
        button_style = ttk.Style()
        button_style.configure("TButton", font=("Arial", 12), width=20)

        # Manage Employees Button
        self.button_employee = ttk.Button(master, text="Manage Employees", command=self.manage_employees)
        self.button_employee.pack(pady=5)

        # Manage Events Button
        self.button_event = ttk.Button(master, text="Manage Events", command=self.manage_events)
        self.button_event.pack(pady=5)

        # Manage Clients Button
        self.button_client = ttk.Button(master, text="Manage Clients", command=self.manage_clients)
        self.button_client.pack(pady=5)

        # Manage Suppliers Button
        self.button_supplier = ttk.Button(master, text="Manage Suppliers", command=self.manage_suppliers)
        self.button_supplier.pack(pady=5)

        # Manage Guests Button
        self.button_guest = ttk.Button(master, text="Manage Guests", command=self.manage_guests)
        self.button_guest.pack(pady=5)

        # Manage Venues Button
        self.button_venue = ttk.Button(master, text="Manage Venues", command=self.manage_venues)
        self.button_venue.pack(pady=5)
        
    # ----------------------------------------------------- employees ----------------------------------------
    def manage_employees(self):
        # Create a new window
        self.employee_window = tk.Toplevel(self.master)
        self.employee_window.title("Manage Employees")

        # Heading for Employees
        self.label_employees = tk.Label(self.employee_window, text="Employees", font=("Arial", 16))
        self.label_employees.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create labels and entry fields for each attribute of Employee
        attributes = ["Name", "Employee ID", "Department", "Job Title", "Basic Salary", "Age", "Date of Birth", "Passport Details"]
        # Create labels and entry fields for each attribute of Employee
        label_name = tk.Label(self.employee_window, text="Name:", font=("Arial", 12))
        label_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_name = tk.Entry(self.employee_window, font=("Arial", 12), width=30)
        entry_name.grid(row=1, column=1, padx=10, pady=5)

        label_employee_id = tk.Label(self.employee_window, text="Employee ID:", font=("Arial", 12))
        label_employee_id.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_employee_id = tk.Entry(self.employee_window, font=("Arial", 12), width=30)
        entry_employee_id.grid(row=2, column=1, padx=10, pady=5)

        label_department = tk.Label(self.employee_window, text="Department:", font=("Arial", 12))
        label_department.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        entry_department = tk.Entry(self.employee_window, font=("Arial", 12), width=30)
        entry_department.grid(row=3, column=1, padx=10, pady=5)

        label_job_title = tk.Label(self.employee_window, text="Job Title:", font=("Arial", 12))
        label_job_title.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        entry_job_title = tk.Entry(self.employee_window, font=("Arial", 12), width=30)
        entry_job_title.grid(row=4, column=1, padx=10, pady=5)

        label_basic_salary = tk.Label(self.employee_window, text="Basic Salary:", font=("Arial", 12))
        label_basic_salary.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        entry_basic_salary = tk.Entry(self.employee_window, font=("Arial", 12), width=30)
        entry_basic_salary.grid(row=5, column=1, padx=10, pady=5)

        label_age = tk.Label(self.employee_window, text="Age:", font=("Arial", 12))
        label_age.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        entry_age = tk.Entry(self.employee_window, font=("Arial", 12), width=30)
        entry_age.grid(row=6, column=1, padx=10, pady=5)

        label_dob = tk.Label(self.employee_window, text="Date of Birth:", font=("Arial", 12))
        label_dob.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        entry_dob = tk.Entry(self.employee_window, font=("Arial", 12), width=30)
        entry_dob.grid(row=7, column=1, padx=10, pady=5)

        label_passport_details = tk.Label(self.employee_window, text="Passport Details:", font=("Arial", 12))
        label_passport_details.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        entry_passport_details = tk.Entry(self.employee_window, font=("Arial", 12), width=30)
        entry_passport_details.grid(row=8, column=1, padx=10, pady=5)

        # Buttons for Add, Update, Delete
        self.button_add = ttk.Button(self.employee_window, text="Add", command=lambda: self.add_employee(
        {
            "Name": entry_name.get(),
            "Employee ID": entry_employee_id.get(),
            "Department": entry_department.get(),
            "Job Title": entry_job_title.get(),
            "Basic Salary": entry_basic_salary.get(),
            "Age": entry_age.get(),
            "Date of Birth": entry_dob.get(),
            "Passport Details": entry_passport_details.get()
        }
        ))
        self.button_add.grid(row=len(attributes)+2, column=0, pady=10)

        self.button_update = ttk.Button(self.employee_window, text="Update", command=lambda: self.update_employee(
            entry_employee_id.get(),
            {
                "Name": entry_name.get(),
                "Employee ID": entry_employee_id.get(),
                "Department": entry_department.get(),
                "Job Title": entry_job_title.get(),
                "Basic Salary": entry_basic_salary.get(),
                "Age": entry_age.get(),
                "Date of Birth": entry_dob.get(),
                "Passport Details": entry_passport_details.get()
            }
        ))
        self.button_update.grid(row=len(attributes)+2, column=1, pady=10)

        self.button_delete = ttk.Button(self.employee_window, text="Delete", command=lambda: self.delete_employee(entry_employee_id.get()))
        self.button_delete.grid(row=len(attributes)+2, column=2, pady=10)

        try:
            with open("employees_data.pickle", "rb") as file:
                employees_data = pickle.load(file)
        except FileNotFoundError:
            employees_data = []
        
        # Treeview Table
        self.tree = ttk.Treeview(self.employee_window, columns=attributes, show="headings")
        for attribute in attributes:
            self.tree.heading(attribute, text=attribute)
        self.tree.grid(row=len(attributes)+3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        
        for employee in employees_data:
            self.tree.insert("", "end", values=(employee["Name"], employee["Employee ID"], employee["Department"], employee["Job Title"], employee["Basic Salary"], employee["Age"], employee["Date of Birth"], employee["Passport Details"]))

        # self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        def on_tree_select(event):
            # Get selected item from Treeview
            selected_item = self.tree.selection()[0]

            # Get data of the selected item
            item_data = self.tree.item(selected_item, "values")

            # Fill up entry fields with selected item data
            entry_name.delete(0, "end")
            entry_name.insert(0, item_data[0])
            entry_employee_id.delete(0, "end")
            entry_employee_id.insert(0, item_data[1])
            entry_department.delete(0, "end")
            entry_department.insert(0, item_data[2])
            entry_job_title.delete(0, "end")
            entry_job_title.insert(0, item_data[3])
            entry_basic_salary.delete(0, "end")
            entry_basic_salary.insert(0, item_data[4])
            entry_age.delete(0, "end")
            entry_age.insert(0, item_data[5])
            entry_dob.delete(0, "end")
            entry_dob.insert(0, item_data[6])
            entry_passport_details.delete(0, "end")
            entry_passport_details.insert(0, item_data[7])

        # Bind the function to handle row selection event
        self.tree.bind("<ButtonRelease-1>", on_tree_select)

    def add_employee(self, employee_data):
        try:
            with open("employees_data.pickle", "rb") as file:
                employees_data = pickle.load(file)
        except FileNotFoundError:
            employees_data = []

        employees_data.append(employee_data)

        with open("employees_data.pickle", "wb") as file:
            pickle.dump(employees_data, file)

        self.refresh_employee_treeview()

    def update_employee(self, selected_item, updated_employee_data):
        with open("employees_data.pickle", "rb") as file:
            employees_data = pickle.load(file)

        for i, employee in enumerate(employees_data):
            if str(employee["Employee ID"]) == str(selected_item):
                employees_data[i] = updated_employee_data
                break

        with open("employees_data.pickle", "wb") as file:
            pickle.dump(employees_data, file)

        self.refresh_employee_treeview()

    def delete_employee(self, selected_item):
        with open("employees_data.pickle", "rb") as file:
            employees_data = pickle.load(file)

        for i, employee in enumerate(employees_data):
            print(selected_item)
            if str(employee["Employee ID"]) == str(selected_item):
                del employees_data[i]
                break

        with open("employees_data.pickle", "wb") as file:
            pickle.dump(employees_data, file)

        self.refresh_employee_treeview()

    def refresh_employee_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            with open("employees_data.pickle", "rb") as file:
                employees_data = pickle.load(file)

            for employee in employees_data:
                self.tree.insert("", "end", values=(employee["Name"], employee["Employee ID"], employee["Department"], employee["Job Title"], employee["Basic Salary"], employee["Age"], employee["Date of Birth"], employee["Passport Details"]))
        except FileNotFoundError:
            pass
    #----------------------------------------------------------event-----------------------------
    def manage_events(self):
        # Create a new window
        self.event_window = tk.Toplevel(self.master)
        self.event_window.title("Manage Events")

        # Heading for Events
        self.label_events = tk.Label(self.event_window, text="Events", font=("Arial", 16))
        self.label_events.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create labels and entry fields for each attribute of Event
        attributes = ["Event ID", "Name", "Date", "Location", "Description"]
        # Create labels and entry fields for each attribute of Event
        label_event_id = tk.Label(self.event_window, text="Event ID:", font=("Arial", 12))
        label_event_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_event_id = tk.Entry(self.event_window, font=("Arial", 12), width=30)
        entry_event_id.grid(row=1, column=1, padx=10, pady=5)

        label_name = tk.Label(self.event_window, text="Name:", font=("Arial", 12))
        label_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_name = tk.Entry(self.event_window, font=("Arial", 12), width=30)
        entry_name.grid(row=2, column=1, padx=10, pady=5)

        label_date = tk.Label(self.event_window, text="Date:", font=("Arial", 12))
        label_date.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        entry_date = tk.Entry(self.event_window, font=("Arial", 12), width=30)
        entry_date.grid(row=3, column=1, padx=10, pady=5)

        label_location = tk.Label(self.event_window, text="Location:", font=("Arial", 12))
        label_location.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        entry_location = tk.Entry(self.event_window, font=("Arial", 12), width=30)
        entry_location.grid(row=4, column=1, padx=10, pady=5)

        label_description = tk.Label(self.event_window, text="Description:", font=("Arial", 12))
        label_description.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        entry_description = tk.Entry(self.event_window, font=("Arial", 12), width=30)
        entry_description.grid(row=5, column=1, padx=10, pady=5)

        # Buttons for Add, Update, Delete
        self.button_add = ttk.Button(self.event_window, text="Add", command=lambda: self.add_event(
            {
                "Event ID": entry_event_id.get(),
                "Name": entry_name.get(),
                "Date": entry_date.get(),
                "Location": entry_location.get(),
                "Description": entry_description.get()
            }
        ))
        self.button_add.grid(row=len(attributes) + 2, column=0, pady=10)

        self.button_update = ttk.Button(self.event_window, text="Update", command=lambda: self.update_event(
            entry_event_id.get(),
            {
                "Event ID": entry_event_id.get(),
                "Name": entry_name.get(),
                "Date": entry_date.get(),
                "Location": entry_location.get(),
                "Description": entry_description.get()
            }
        ))
        self.button_update.grid(row=len(attributes) + 2, column=1, pady=10)

        self.button_delete = ttk.Button(self.event_window, text="Delete", command=lambda: self.delete_event(entry_event_id.get()))
        self.button_delete.grid(row=len(attributes) + 2, column=2, pady=10)

        try:
            with open("events_data.pickle", "rb") as file:
                events_data = pickle.load(file)
        except FileNotFoundError:
            events_data = []

        # Treeview Table
        self.tree = ttk.Treeview(self.event_window, columns=attributes, show="headings")
        for attribute in attributes:
            self.tree.heading(attribute, text=attribute)
        self.tree.grid(row=len(attributes) + 3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Insert data into the Treeview
        for event in events_data:
            self.tree.insert("", "end", values=(event["Event ID"], event["Name"], event["Date"], event["Location"], event["Description"]))

        def on_tree_select(event):
            # Get selected item from Treeview
            selected_item = self.tree.selection()[0]

            # Get data of the selected item
            item_data = self.tree.item(selected_item, "values")

            # Fill up entry fields with selected item data
            entry_event_id.delete(0, "end")
            entry_event_id.insert(0, item_data[0])
            entry_name.delete(0, "end")
            entry_name.insert(0, item_data[1])
            entry_date.delete(0, "end")
            entry_date.insert(0, item_data[2])
            entry_location.delete(0, "end")
            entry_location.insert(0, item_data[3])
            entry_description.delete(0, "end")
            entry_description.insert(0, item_data[4])

        # Bind the function to handle row selection event
        self.tree.bind("<ButtonRelease-1>", on_tree_select)
    def add_event(self, event_data):
        try:
            with open("events_data.pickle", "rb") as file:
                events_data = pickle.load(file)
        except FileNotFoundError:
            events_data = []

        events_data.append(event_data)

        with open("events_data.pickle", "wb") as file:
            pickle.dump(events_data, file)

        self.refresh_event_treeview()

    def update_event(self, selected_item, updated_event_data):
        with open("events_data.pickle", "rb") as file:
            events_data = pickle.load(file)

        for i, event in enumerate(events_data):
            if str(event["Event ID"]) == str(selected_item):
                events_data[i] = updated_event_data
                break

        with open("events_data.pickle", "wb") as file:
            pickle.dump(events_data, file)

        self.refresh_event_treeview()

    def delete_event(self, selected_item):
        with open("events_data.pickle", "rb") as file:
            events_data = pickle.load(file)

        for i, event in enumerate(events_data):
            if str(event["Event ID"]) == str(selected_item):
                del events_data[i]
                break

        with open("events_data.pickle", "wb") as file:
            pickle.dump(events_data, file)

        self.refresh_event_treeview()

    def refresh_event_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            with open("events_data.pickle", "rb") as file:
                events_data = pickle.load(file)

            for event in events_data:
                self.tree.insert("", "end", values=(event["Event ID"], event["Name"], event["Date"], event["Location"], event["Description"]))
        except FileNotFoundError:
            pass
    
     # ------------------------------------------------------ clients ---------------------------------
    def manage_clients(self):
        # Create a new window
        self.client_window = tk.Toplevel(self.master)
        self.client_window.title("Manage Clients")

        # Heading for Clients
        self.label_clients = tk.Label(self.client_window, text="Clients", font=("Arial", 16))
        self.label_clients.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create labels and entry fields for each attribute of Client
        attributes = ["Client ID", "Name", "Email", "Phone"]
        # Create labels and entry fields for each attribute of Client
        label_client_id = tk.Label(self.client_window, text="Client ID:", font=("Arial", 12))
        label_client_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_client_id = tk.Entry(self.client_window, font=("Arial", 12), width=30)
        entry_client_id.grid(row=1, column=1, padx=10, pady=5)

        label_name = tk.Label(self.client_window, text="Name:", font=("Arial", 12))
        label_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_name = tk.Entry(self.client_window, font=("Arial", 12), width=30)
        entry_name.grid(row=2, column=1, padx=10, pady=5)

        label_email = tk.Label(self.client_window, text="Email:", font=("Arial", 12))
        label_email.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        entry_email = tk.Entry(self.client_window, font=("Arial", 12), width=30)
        entry_email.grid(row=3, column=1, padx=10, pady=5)

        label_phone = tk.Label(self.client_window, text="Phone:", font=("Arial", 12))
        label_phone.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        entry_phone = tk.Entry(self.client_window, font=("Arial", 12), width=30)
        entry_phone.grid(row=4, column=1, padx=10, pady=5)

        # Buttons for Add, Update, Delete
        self.button_add = ttk.Button(self.client_window, text="Add", command=lambda: self.add_client(
            {
                "Client ID": entry_client_id.get(),
                "Name": entry_name.get(),
                "Email": entry_email.get(),
                "Phone": entry_phone.get()
            }
        ))
        self.button_add.grid(row=len(attributes)+2, column=0, pady=10)

        self.button_update = ttk.Button(self.client_window, text="Update", command=lambda: self.update_client(
            entry_client_id.get(),
            {
                "Client ID": entry_client_id.get(),
                "Name": entry_name.get(),
                "Email": entry_email.get(),
                "Phone": entry_phone.get()
            }
        ))
        self.button_update.grid(row=len(attributes)+2, column=1, pady=10)

        self.button_delete = ttk.Button(self.client_window, text="Delete", command=lambda: self.delete_client(entry_client_id.get()))
        self.button_delete.grid(row=len(attributes)+2, column=2, pady=10)

        try:
            with open("clients_data.pickle", "rb") as file:
                clients_data = pickle.load(file)
        except FileNotFoundError:
            clients_data = []
        
        # Treeview Table
        self.tree = ttk.Treeview(self.client_window, columns=attributes, show="headings")
        for attribute in attributes:
            self.tree.heading(attribute, text=attribute)
        self.tree.grid(row=len(attributes)+3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        for client in clients_data:
            self.tree.insert("", "end", values=(client["Client ID"], client["Name"], client["Email"], client["Phone"]))
            
        def on_tree_select_client(event):
            # Get selected item from Treeview
            selected_item = self.tree.selection()[0]

            # Get data of the selected item
            item_data = self.tree.item(selected_item, "values")

            # Fill up entry fields with selected item data
            entry_client_id.delete(0, "end")
            entry_client_id.insert(0, item_data[0])
            entry_name.delete(0, "end")
            entry_name.insert(0, item_data[1])
            entry_email.delete(0, "end")
            entry_email.insert(0, item_data[2])
            entry_phone.delete(0, "end")
            entry_phone.insert(0, item_data[3])

        # Bind the function to handle row selection event
        self.tree.bind("<ButtonRelease-1>", on_tree_select_client)

    def add_client(self, client_data):
        try:
            with open("clients_data.pickle", "rb") as file:
                clients_data = pickle.load(file)
        except FileNotFoundError:
            clients_data = []

        clients_data.append(client_data)

        with open("clients_data.pickle", "wb") as file:
            pickle.dump(clients_data, file)

        self.refresh_client_treeview()

    def update_client(self, selected_item, updated_client_data):
        with open("clients_data.pickle", "rb") as file:
            clients_data = pickle.load(file)

        for i, client in enumerate(clients_data):
            if str(client["Client ID"]) == str(selected_item):
                clients_data[i] = updated_client_data
                break

        with open("clients_data.pickle", "wb") as file:
            pickle.dump(clients_data, file)

        self.refresh_client_treeview()

    def delete_client(self, selected_item):
        with open("clients_data.pickle", "rb") as file:
            clients_data = pickle.load(file)

        for i, client in enumerate(clients_data):
            if str(client["Client ID"]) == str(selected_item):
                del clients_data[i]
                break

        with open("clients_data.pickle", "wb") as file:
            pickle.dump(clients_data, file)

        self.refresh_client_treeview()

    def refresh_client_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            with open("clients_data.pickle", "rb") as file:
                clients_data = pickle.load(file)

            for client in clients_data:
                self.tree.insert("", "end", values=(client["Client ID"], client["Name"], client["Email"], client["Phone"]))
        except FileNotFoundError:
            pass
     # ------------------------------------------------------ suppliers ---------------------------------
    def manage_suppliers(self):
        # Create a new window
        self.supplier_window = tk.Toplevel(self.master)
        self.supplier_window.title("Manage Suppliers")

        # Heading for Suppliers
        self.label_suppliers = tk.Label(self.supplier_window, text="Suppliers", font=("Arial", 16))
        self.label_suppliers.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create labels and entry fields for each attribute of Supplier
        attributes = ["Supplier ID", "Name", "Products", "Contact Person", "Email", "Phone"]
        # Create labels and entry fields for each attribute of Supplier
        label_supplier_id = tk.Label(self.supplier_window, text="Supplier ID:", font=("Arial", 12))
        label_supplier_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_supplier_id = tk.Entry(self.supplier_window, font=("Arial", 12), width=30)
        entry_supplier_id.grid(row=1, column=1, padx=10, pady=5)

        label_name = tk.Label(self.supplier_window, text="Name:", font=("Arial", 12))
        label_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_name = tk.Entry(self.supplier_window, font=("Arial", 12), width=30)
        entry_name.grid(row=2, column=1, padx=10, pady=5)

        label_products = tk.Label(self.supplier_window, text="Products:", font=("Arial", 12))
        label_products.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        entry_products = tk.Entry(self.supplier_window, font=("Arial", 12), width=30)
        entry_products.grid(row=3, column=1, padx=10, pady=5)

        label_contact_person = tk.Label(self.supplier_window, text="Contact Person:", font=("Arial", 12))
        label_contact_person.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        entry_contact_person = tk.Entry(self.supplier_window, font=("Arial", 12), width=30)
        entry_contact_person.grid(row=4, column=1, padx=10, pady=5)

        label_email = tk.Label(self.supplier_window, text="Email:", font=("Arial", 12))
        label_email.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        entry_email = tk.Entry(self.supplier_window, font=("Arial", 12), width=30)
        entry_email.grid(row=5, column=1, padx=10, pady=5)

        label_phone = tk.Label(self.supplier_window, text="Phone:", font=("Arial", 12))
        label_phone.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        entry_phone = tk.Entry(self.supplier_window, font=("Arial", 12), width=30)
        entry_phone.grid(row=6, column=1, padx=10, pady=5)
        # Buttons for Add, Update, Delete
        self.button_add = ttk.Button(self.supplier_window, text="Add", command=lambda: self.add_supplier(entry_supplier_id, entry_name, entry_products, entry_contact_person, entry_email, entry_phone))
        self.button_add.grid(row=len(attributes)+2, column=0, pady=10)

        self.button_update = ttk.Button(self.supplier_window, text="Update", command=lambda: self.update_supplier(entry_supplier_id, entry_name, entry_products, entry_contact_person, entry_email, entry_phone))
        self.button_update.grid(row=len(attributes)+2, column=1, pady=10)

        self.button_delete = ttk.Button(self.supplier_window, text="Delete", command=lambda: self.delete_supplier(entry_supplier_id))
        self.button_delete.grid(row=len(attributes)+2, column=2, pady=10)
        
        try:
            with open("suppliers_data.pickle", "rb") as file:
                suppliers_data = pickle.load(file)
        except FileNotFoundError:
            suppliers_data = []
        
        # Treeview Table
        self.tree = ttk.Treeview(self.supplier_window, columns=attributes, show="headings")
        for attribute in attributes:
            self.tree.heading(attribute, text=attribute)
        self.tree.grid(row=len(attributes)+3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        for supplier in suppliers_data:
            self.tree.insert("", "end", values=(supplier["Supplier ID"], supplier["Name"], supplier["Products"], supplier["Contact Person"], supplier["Email"], supplier["Phone"]))

        def on_tree_select_supplier(event):
            # Get selected item from Treeview
            selected_item = self.tree.selection()[0]

            # Get data of the selected item
            item_data = self.tree.item(selected_item, "values")

            # Fill up entry fields with selected item data
            entry_supplier_id.delete(0, "end")
            entry_supplier_id.insert(0, item_data[0])
            entry_name.delete(0, "end")
            entry_name.insert(0, item_data[1])
            entry_products.delete(0, "end")
            entry_products.insert(0, item_data[2])
            entry_contact_person.delete(0, "end")
            entry_contact_person.insert(0, item_data[3])
            entry_email.delete(0, "end")
            entry_email.insert(0, item_data[4])
            entry_phone.delete(0, "end")
            entry_phone.insert(0, item_data[5])

        # Bind the function to handle row selection event
        self.tree.bind("<ButtonRelease-1>", on_tree_select_supplier)

    def add_supplier(self, entry_supplier_id, entry_name, entry_products, entry_contact_person, entry_email, entry_phone):
        supplier_data = {
            "Supplier ID": entry_supplier_id.get(),
            "Name": entry_name.get(),
            "Products": entry_products.get(),
            "Contact Person": entry_contact_person.get(),
            "Email": entry_email.get(),
            "Phone": entry_phone.get()
        }
        try:
            with open("suppliers_data.pickle", "rb") as file:
                suppliers_data = pickle.load(file)
        except FileNotFoundError:
            suppliers_data = []

        suppliers_data.append(supplier_data)

        with open("suppliers_data.pickle", "wb") as file:
            pickle.dump(suppliers_data, file)

        self.refresh_supplier_treeview()

    def update_supplier(self, entry_supplier_id, entry_name, entry_products, entry_contact_person, entry_email, entry_phone):
        updated_supplier_data = {
            "Supplier ID": entry_supplier_id.get(),
            "Name": entry_name.get(),
            "Products": entry_products.get(),
            "Contact Person": entry_contact_person.get(),
            "Email": entry_email.get(),
            "Phone": entry_phone.get()
        }
        with open("suppliers_data.pickle", "rb") as file:
            suppliers_data = pickle.load(file)

        for i, supplier in enumerate(suppliers_data):
            if str(supplier["Supplier ID"]) == str(entry_supplier_id.get()):
                suppliers_data[i] = updated_supplier_data
                break

        with open("suppliers_data.pickle", "wb") as file:
            pickle.dump(suppliers_data, file)

        self.refresh_supplier_treeview()

    def delete_supplier(self, entry_supplier_id):
        with open("suppliers_data.pickle", "rb") as file:
            suppliers_data = pickle.load(file)

        for i, supplier in enumerate(suppliers_data):
            if str(supplier["Supplier ID"]) == str(entry_supplier_id.get()):
                del suppliers_data[i]
                break

        with open("suppliers_data.pickle", "wb") as file:
            pickle.dump(suppliers_data, file)

        self.refresh_supplier_treeview()

    def refresh_supplier_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            with open("suppliers_data.pickle", "rb") as file:
                suppliers_data = pickle.load(file)

            for supplier in suppliers_data:
                self.tree.insert("", "end", values=(supplier["Supplier ID"], supplier["Name"], supplier["Products"], supplier["Contact Person"], supplier["Email"], supplier["Phone"]))
        except FileNotFoundError:
            pass

     # ------------------------------------------------------ guests ---------------------------------
    def manage_guests(self):
        # Create a new window
        self.guest_window = tk.Toplevel(self.master)
        self.guest_window.title("Manage Guests")

        # Heading for Guests
        self.label_guests = tk.Label(self.guest_window, text="Guests", font=("Arial", 16))
        self.label_guests.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create labels and entry fields for each attribute of Guest
        attributes = ["Guest ID", "Name", "Email", "Phone"]
        # Create labels and entry fields for each attribute of Guest
        label_guest_id = tk.Label(self.guest_window, text="Guest ID:", font=("Arial", 12))
        label_guest_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_guest_id = tk.Entry(self.guest_window, font=("Arial", 12), width=30)
        entry_guest_id.grid(row=1, column=1, padx=10, pady=5)

        label_name = tk.Label(self.guest_window, text="Name:", font=("Arial", 12))
        label_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_name = tk.Entry(self.guest_window, font=("Arial", 12), width=30)
        entry_name.grid(row=2, column=1, padx=10, pady=5)

        label_email = tk.Label(self.guest_window, text="Email:", font=("Arial", 12))
        label_email.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        entry_email = tk.Entry(self.guest_window, font=("Arial", 12), width=30)
        entry_email.grid(row=3, column=1, padx=10, pady=5)

        label_phone = tk.Label(self.guest_window, text="Phone:", font=("Arial", 12))
        label_phone.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        entry_phone = tk.Entry(self.guest_window, font=("Arial", 12), width=30)
        entry_phone.grid(row=4, column=1, padx=10, pady=5)
        
        # Buttons for Add, Update, Delete
        self.button_add = ttk.Button(self.guest_window, text="Add", command=lambda: self.add_guest(entry_guest_id, entry_name, entry_email, entry_phone))
        self.button_add.grid(row=len(attributes)+2, column=0, pady=10)

        self.button_update = ttk.Button(self.guest_window, text="Update", command=lambda: self.update_guest(entry_guest_id, entry_name, entry_email, entry_phone))
        self.button_update.grid(row=len(attributes)+2, column=1, pady=10)

        self.button_delete = ttk.Button(self.guest_window, text="Delete", command=lambda: self.delete_guest(entry_guest_id))
        self.button_delete.grid(row=len(attributes)+2, column=2, pady=10)

        try:
            with open("guests_data.pickle", "rb") as file:
                guests_data = pickle.load(file)
        except FileNotFoundError:
            guests_data = []
        
        # Treeview Table
        self.tree = ttk.Treeview(self.guest_window, columns=attributes, show="headings")
        for attribute in attributes:
            self.tree.heading(attribute, text=attribute)
        self.tree.grid(row=len(attributes)+3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        
        for guest in guests_data:
            self.tree.insert("", "end", values=(guest["Guest ID"], guest["Name"], guest["Email"], guest["Phone"]))

        def on_tree_select_guest(event):
            # Get selected item from Treeview
            selected_item = self.tree.selection()[0]

            # Get data of the selected item
            item_data = self.tree.item(selected_item, "values")

            # Fill up entry fields with selected item data
            entry_guest_id.delete(0, "end")
            entry_guest_id.insert(0, item_data[0])
            entry_name.delete(0, "end")
            entry_name.insert(0, item_data[1])
            entry_email.delete(0, "end")
            entry_email.insert(0, item_data[2])
            entry_phone.delete(0, "end")
            entry_phone.insert(0, item_data[3])

        # Bind the function to handle row selection event
        self.tree.bind("<ButtonRelease-1>", on_tree_select_guest)

    def add_guest(self, entry_guest_id, entry_name, entry_email, entry_phone):
        guest_data = {
            "Guest ID": entry_guest_id.get(),
            "Name": entry_name.get(),
            "Email": entry_email.get(),
            "Phone": entry_phone.get()
        }
        try:
            with open("guests_data.pickle", "rb") as file:
                guests_data = pickle.load(file)
        except FileNotFoundError:
            guests_data = []

        guests_data.append(guest_data)

        with open("guests_data.pickle", "wb") as file:
            pickle.dump(guests_data, file)

        self.refresh_guest_treeview()

    def update_guest(self, entry_guest_id, entry_name, entry_email, entry_phone):
        updated_guest_data = {
            "Guest ID": entry_guest_id.get(),
            "Name": entry_name.get(),
            "Email": entry_email.get(),
            "Phone": entry_phone.get()
        }
        with open("guests_data.pickle", "rb") as file:
            guests_data = pickle.load(file)

        for i, guest in enumerate(guests_data):
            if str(guest["Guest ID"]) == str(entry_guest_id.get()):
                guests_data[i] = updated_guest_data
                break

        with open("guests_data.pickle", "wb") as file:
            pickle.dump(guests_data, file)

        self.refresh_guest_treeview()

    def delete_guest(self, entry_guest_id):
        with open("guests_data.pickle", "rb") as file:
            guests_data = pickle.load(file)

        for i, guest in enumerate(guests_data):
            if str(guest["Guest ID"]) == str(entry_guest_id.get()):
                del guests_data[i]
                break

        with open("guests_data.pickle", "wb") as file:
            pickle.dump(guests_data, file)

        self.refresh_guest_treeview()

    def refresh_guest_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            with open("guests_data.pickle", "rb") as file:
                guests_data = pickle.load(file)

            for guest in guests_data:
                self.tree.insert("", "end", values=(guest["Guest ID"], guest["Name"], guest["Email"], guest["Phone"]))
        except FileNotFoundError:
            pass

     # ------------------------------------------------------ venues ---------------------------------
    def manage_venues(self):
        # Create a new window
        self.venue_window = tk.Toplevel(self.master)
        self.venue_window.title("Manage Venues")

        # Heading for Venues
        self.label_venues = tk.Label(self.venue_window, text="Venues", font=("Arial", 16))
        self.label_venues.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create labels and entry fields for each attribute of Venue
        attributes = ["Venue ID", "Name", "Location", "Capacity", "Contact Person", "Email", "Phone"]
        # Create labels and entry fields for each attribute of Venue
        label_venue_id = tk.Label(self.venue_window, text="Venue ID:", font=("Arial", 12))
        label_venue_id.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_venue_id = tk.Entry(self.venue_window, font=("Arial", 12), width=30)
        entry_venue_id.grid(row=1, column=1, padx=10, pady=5)

        label_name = tk.Label(self.venue_window, text="Name:", font=("Arial", 12))
        label_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_name = tk.Entry(self.venue_window, font=("Arial", 12), width=30)
        entry_name.grid(row=2, column=1, padx=10, pady=5)

        label_location = tk.Label(self.venue_window, text="Location:", font=("Arial", 12))
        label_location.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        entry_location = tk.Entry(self.venue_window, font=("Arial", 12), width=30)
        entry_location.grid(row=3, column=1, padx=10, pady=5)

        label_capacity = tk.Label(self.venue_window, text="Capacity:", font=("Arial", 12))
        label_capacity.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        entry_capacity = tk.Entry(self.venue_window, font=("Arial", 12), width=30)
        entry_capacity.grid(row=4, column=1, padx=10, pady=5)

        label_contact_person = tk.Label(self.venue_window, text="Contact Person:", font=("Arial", 12))
        label_contact_person.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        entry_contact_person = tk.Entry(self.venue_window, font=("Arial", 12), width=30)
        entry_contact_person.grid(row=5, column=1, padx=10, pady=5)

        label_email = tk.Label(self.venue_window, text="Email:", font=("Arial", 12))
        label_email.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        entry_email = tk.Entry(self.venue_window, font=("Arial", 12), width=30)
        entry_email.grid(row=6, column=1, padx=10, pady=5)

        label_phone = tk.Label(self.venue_window, text="Phone:", font=("Arial", 12))
        label_phone.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        entry_phone = tk.Entry(self.venue_window, font=("Arial", 12), width=30)
        entry_phone.grid(row=7, column=1, padx=10, pady=5)

        # Buttons for Add, Update, Delete
        self.button_add = ttk.Button(self.venue_window, text="Add", command=lambda: self.add_venue(entry_venue_id.get(), entry_name.get(), entry_location.get(), entry_capacity.get(), entry_contact_person.get(), entry_email.get(), entry_phone.get()))
        self.button_add.grid(row=len(attributes)+2, column=0, pady=10)

        self.button_update = ttk.Button(self.venue_window, text="Update", command=lambda: self.update_venue(entry_venue_id.get(), entry_name.get(), entry_location.get(), entry_capacity.get(), entry_contact_person.get(), entry_email.get(), entry_phone.get()))
        self.button_update.grid(row=len(attributes)+2, column=1, pady=10)

        self.button_delete = ttk.Button(self.venue_window, text="Delete", command=lambda: self.delete_venue(entry_venue_id.get()))
        self.button_delete.grid(row=len(attributes)+2, column=2, pady=10)
        try:
            with open("venues_data.pickle", "rb") as file:
                venues_data = pickle.load(file)
        except FileNotFoundError:
            venues_data = []
        
        # Treeview Table
        self.tree = ttk.Treeview(self.venue_window, columns=attributes, show="headings")
        for attribute in attributes:
            self.tree.heading(attribute, text=attribute)
        self.tree.grid(row=len(attributes)+3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        for venue in venues_data:
            self.tree.insert("", "end", values=(venue["Venue ID"], venue["Name"], venue["Location"], venue["Capacity"], venue["Contact Person"], venue["Email"], venue["Phone"]))

        def on_tree_select_venue(event):
            # Get selected item from Treeview
            selected_item = self.tree.selection()[0]

            # Get data of the selected item
            item_data = self.tree.item(selected_item, "values")

            # Fill up entry fields with selected item data
            entry_venue_id.delete(0, "end")
            entry_venue_id.insert(0, item_data[0])
            entry_name.delete(0, "end")
            entry_name.insert(0, item_data[1])
            entry_location.delete(0, "end")
            entry_location.insert(0, item_data[2])
            entry_capacity.delete(0, "end")
            entry_capacity.insert(0, item_data[3])
            entry_contact_person.delete(0, "end")
            entry_contact_person.insert(0, item_data[4])
            entry_email.delete(0, "end")
            entry_email.insert(0, item_data[5])
            entry_phone.delete(0, "end")
            entry_phone.insert(0, item_data[6])

        # Bind the function to handle row selection event
        self.tree.bind("<ButtonRelease-1>", on_tree_select_venue)
        
    def refresh_venues(self):
        # Clear existing items in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Reload data from the file
        try:
            with open("venues_data.pickle", "rb") as file:
                venues_data = pickle.load(file)
        except FileNotFoundError:
            venues_data = []
        # Insert data into the treeview
        for venue in venues_data:
            self.tree.insert("", "end", values=(venue["Venue ID"], venue["Name"], venue["Location"], venue["Capacity"], venue["Contact Person"], venue["Email"], venue["Phone"]))

    def add_venue(self, venue_id, name, location, capacity, contact_person, email, phone):
        # Create a new venue dictionary
        new_venue = {
            "Venue ID": venue_id,
            "Name": name,
            "Location": location,
            "Capacity": capacity,
            "Contact Person": contact_person,
            "Email": email,
            "Phone": phone
        }
        # Append the new venue to the venues data list
        try:
            with open("venues_data.pickle", "rb") as file:
                venues_data = pickle.load(file)
        except FileNotFoundError:
            venues_data = []
        venues_data.append(new_venue)
        # Save the updated venues data to the file
        with open("venues_data.pickle", "wb") as file:
            pickle.dump(venues_data, file)
        # Refresh the venues data in the treeview
        self.refresh_venues()
        # Clear the entry fields


    def update_venue(self, venue_id, name, location, capacity, contact_person, email, phone):
        try:
            with open("venues_data.pickle", "rb") as file:
                venues_data = pickle.load(file)
        except FileNotFoundError:
            return
        # Find the index of the venue to update
        for i, venue in enumerate(venues_data):
            if str(venue["Venue ID"]) == str(venue_id):
                # Update the venue details
                venues_data[i]["Name"] = name
                venues_data[i]["Location"] = location
                venues_data[i]["Capacity"] = capacity
                venues_data[i]["Contact Person"] = contact_person
                venues_data[i]["Email"] = email
                venues_data[i]["Phone"] = phone
                break
        # Save the updated venues data to the file
        with open("venues_data.pickle", "wb") as file:
            pickle.dump(venues_data, file)
        # Refresh the venues data in the treeview
        self.refresh_venues()
        # Clear the entry fields

    def delete_venue(self, venue_id):
        try:
            with open("venues_data.pickle", "rb") as file:
                venues_data = pickle.load(file)
        except FileNotFoundError:
            return
        # Find the index of the venue to delete
        for i, venue in enumerate(venues_data):
            if str(venue["Venue ID"]) == str(venue_id):
                del venues_data[i]
                break
        # Save the updated venues data to the file
        with open("venues_data.pickle", "wb") as file:
            pickle.dump(venues_data, file)
        # Refresh the venues data in the treeview
        self.refresh_venues()
        # Clear the entry fields


    
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementGUI(root)
    root.mainloop()
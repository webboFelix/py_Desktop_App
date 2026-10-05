from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

# functions
def populate_list():
    part_list.delete(0, END)
    for row in db.fetch():
        part_list.insert(END, row)

def add_item():
    if part_text.get()=='' or customer_text.get()=='' or retailer_text.get()=='' or price_text.get()=='':
        messagebox.showerror('Required Fields!', 'Please include all fields')
        return
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    part_list.delete(0, END)
    part_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    clear_fields()
    populate_list()
    
def select_item(event):
    try:
        global selected_item
        index = part_list.curselection()[0]
        selected_item = part_list.get(index)
        
        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_fields()
    populate_list()

def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    clear_fields()
    populate_list()

def clear_fields():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)


# create the main window
app = Tk()

#App
part_text = StringVar()
part_label = Label(app, text="Part", font=("bold", 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text, width=50)
part_entry.grid(row=0, column=1)

#customer
customer_text = StringVar()
customer_label = Label(app, text="Customer", font=("bold", 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text, width=50)
customer_entry.grid(row=0, column=3)

#Retailer
retailer_text = StringVar()
retailer_label = Label(app, text="Retailer", font=("bold", 14))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text, width=50)
retailer_entry.grid(row=1, column=1)

#Price
price_text = StringVar()
price_label = Label(app, text="Price", font=("bold", 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text, width=50)
price_entry.grid(row=1, column=3)

# app listbox
part_list = Listbox(app, height=8, width=50)
part_list.grid(row=3, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

# bind select
part_list.bind('<<ListboxSelect>>', select_item)
# create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# link scrollbar to listbox
part_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_list.yview)

# buttons
add_button = Button(app, text="Add", width=12, command=add_item)
add_button.grid(row=2, column=0, pady=20)

remove_button = Button(app, text="Remove", width=12, command=remove_item)
remove_button.grid(row=2, column=1, pady=20)

update_button = Button(app, text="Update", width=12, command=update_item)
update_button.grid(row=2, column=2, pady=20)

clear_button = Button(app, text="Clear", width=12, command=clear_fields)
clear_button.grid(row=2, column=3, pady=20)


app.title("My Application")
app.geometry("700x350")

# populate initial list
populate_list()

# start the main event loop
app.mainloop()
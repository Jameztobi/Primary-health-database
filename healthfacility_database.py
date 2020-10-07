import tkinter as tk
from tkinter import filedialog, Text
import os
import sqlite3

root=tk.Tk()
root.geometry("350x400")
#database



#create Table
'''
c.execute(""" CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
'''

def save():
    conn=sqlite3.connect("address_book.db") # create a database or connect to one
    c=conn.cursor()   #create cursor
    
    record_id=delete_box.get()
    
    c.execute("""UPDATE addresses SET
    first_name =:first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode= :zipcode

    WHERE oid = :oid""",
    {
    "first": f_name_editor.get(),
    "last": l_name_editor.get(),
    "address": address_editor.get(),
    "city": city_editor.get(),
    "state": state_editor.get(),
    "zipcode": zipcode_editor.get(),
    "oid": record_id
    } )

    conn.commit()    #commit changes 
    conn.close()   #close connection
    
    editor.destroy()
   



def edit():
    global editor
    editor=tk.Toplevel()
    editor.geometry("350x400")
    editor.title("Update A Record")
    
    conn=sqlite3.connect("address_book.db") # create a database or connect to one
    c=conn.cursor()    

    record_id=delete_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records=c.fetchall()
    
     #Create Global variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor


#create  Text Boxes
    f_name_editor=tk.Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor=tk.Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor=tk.Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor=tk.Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor=tk.Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor=tk.Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

# create Text Box labels
    f_name_label=tk.Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0)
    l_name_label=tk.Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label=tk.Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label=tk.Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label=tk.Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label=tk.Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
     
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


#create a Save Button To  Save edited record
    edit_btn=tk.Button(editor, text="Save record", command=save)
    edit_btn.grid(row=6, column=0, pady=10, columnspan=2, padx=10, ipadx=135)
    

#funct to delete
def delete():
    conn=sqlite3.connect("address_book.db") # create a database or connect to one
    c=conn.cursor()   #create cursor
    c.execute("DELETE FROM addresses WHERE oid= " + delete_box.get())

    conn.commit()    #commit changes 
    conn.close()   #close connection
   

#create submit function 
def submit():
    conn=sqlite3.connect("address_book.db") # create a database or connect to one
    c=conn.cursor()   #create cursor
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
    {
        "f_name": f_name.get(),
        "l_name": l_name.get(),
        "address": address.get(),
        "city": city.get(),
        "state": state.get(),
        "zipcode": zipcode.get()
    } )

    conn.commit()    #commit changes 
    conn.close()   #close connection

    f_name.delete(0, "end")
    l_name.delete(0, "end")
    address.delete(0, "end")
    city.delete(0, "end")
    state.delete(0, "end")
    zipcode.delete(0, "end")
 
 #define query
def query():
    conn=sqlite3.connect("address_book.db") # create a database or connect to one
    c=conn.cursor()    
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records=c.fetchall()
    #print(records)

    #loop through results
    print_records= ''
    for record in records:
        print_records+= str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6])+ "\n"

    query_label= tk.Label(root, text=print_records)
    query_label.grid(row=11, column=0,  columnspan=2)
    

# create Entry Boxes
f_name=tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name=tk.Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address=tk.Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city=tk.Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state=tk.Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode=tk.Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box=tk.Entry(root, width=30)
delete_box.grid(row=9, column=1, padx=20)

# create Text Box labels
f_name_label=tk.Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label=tk.Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label=tk.Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label=tk.Label(root, text="City")
city_label.grid(row=3, column=0)
state_label=tk.Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label=tk.Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label=tk.Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=10)


# create submit button
submit_btn =tk.Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create a query Button
query_btn =tk.Button(root, text="show record", command=query)
query_btn.grid(row=7, column=0, pady=10, columnspan=2, padx=10, ipadx=137)

#create a delete button
delete_btn =tk.Button(root, text="Delete record", command=delete)
delete_btn.grid(row=10, column=0, pady=10, columnspan=2, padx=10, ipadx=135)

#create an Update Button
edit_btn=tk.Button(root, text="Edit record", command=edit)
edit_btn.grid(row=11, column=0, pady=10, columnspan=2, padx=10, ipadx=135)

root.mainloop()
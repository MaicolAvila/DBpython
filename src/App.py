from tkinter import *
import psycopg2
import tkinter as tk
from tkinter import ttk
from tabulate import tabulate

root = Tk()
root.title("GestAPP")






#funcion de buscar
def search(id):
     #crear conexion
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="maicol82",
        host="localhost",
        port="5432"
    )
    #funcion cursor
    cursor = conn.cursor()
    query = '''SELECT * FROM casos WHERE id=%s'''
    cursor.execute(query, (id))

    
    
    row = cursor.fetchall()
    listbox = Listbox(frame, width=80, heigh=5)
    listbox.grid(row=15, columnspan=10, sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    print(tabulate(row))
    conn.commit()
    conn.close()

def display_search_result(row):
    listbox = Listbox(frame, width=80, heigh=3)
    listbox.grid(row=15, column=10, sticky=W+E)
    listbox.insert(END, row)

#funcion guardar datos
def save_new_case(Caso, Nombre, Telefono, Direccion, Afectacion, Estado):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="maicol82",
        host="localhost",
        port="5432"
    )
    #funcion cursor
    cursor = conn.cursor()
    query = '''INSERT INTO casos(caso, nombre, telefono, direccion, afectacion, estado) VALUES (%s, %s, %s, %s, %s, %s)'''
    cursor.execute(query, (Caso, Nombre, Telefono, Direccion, Afectacion, Estado))
    print("Data saved")
    conn.commit()
    conn.close()
    #refrescar la funcion de mostrar
    display_table_casos()

#funcion para mostrar tabla
def display_table_casos():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="maicol82",
        host="localhost",
        port="5432"
    )
    #funcion cursor
    cursor = conn.cursor()
    query = '''SELECT * FROM casos'''
    cursor.execute(query)

    row = cursor.fetchall()
    print(tabulate(row))
    listbox = Listbox(frame, width=80, heigh=5)
    listbox.grid(row=25, columnspan=10, sticky=W+E)

    for x in row:
        listbox.insert(END, x)

       
    conn.commit()
    conn.close()
    
def delete(id):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="maicol82",
        host="localhost",
        port="5432"
    )
    #funcion cursor
    cursor = conn.cursor()
    query = '''DELETE FROM casos WHERE id=%s'''
    cursor.execute(query, (id))

    conn.commit()
    conn.close()
    #refrescar la funcion de mostrar
    display_table_casos()

#canvas
canvas = Canvas(root, height=700, width=600)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Add a caso')
label.grid(row=0, column=2)

#numero de caso
label = Label(frame, text="Caso")
label.grid(row=1, column=0)

entry_caso = Entry(frame)
entry_caso.grid(row=1, column=1)

#nombre
label = Label(frame, text="Nombre")
label.grid(row=2, column=0)

entry_nombre = Entry(frame)
entry_nombre.grid(row=2, column=1)

#Telefono
label = Label(frame, text="Telefono")
label.grid(row=3, column=0)

entry_telefono = Entry(frame)
entry_telefono.grid(row=3, column=1)

#Direccion
label = Label(frame, text="Direccion")
label.grid(row=1, column=2)

entry_direccion = Entry(frame)
entry_direccion.grid(row=1, column=3)

#Afectacion
label = Label(frame, text="Afectacion")
label.grid(row=2, column=2)

entry_afectacion = Entry(frame)
entry_afectacion.grid(row=2, column=3)

#Estado
label = Label(frame, text="Estado")
label.grid(row=3, column=2)

entry_estado = Entry(frame)
entry_estado.grid(row=3, column=3)

#Button of save
button = Button(frame, text="Add", backgroun="#0575E6", command=lambda:save_new_case(
    entry_caso.get(),
    entry_nombre.get(),
    entry_telefono.get(),
    entry_direccion.get(),
    entry_afectacion.get(),
    entry_estado.get()   
    ))
button.grid(row=7, column=2, sticky=W+E)

#Search
label = Label(frame, text="Search Data")
label.grid(row=8, column=0)

label = Label(frame, text="Search By Case")
label.grid(row=9, column=0)

id_search = Entry(frame)
id_search.grid(row=9, column=1 )

button = Button(frame, text="Search", command=lambda:search(id_search.get()))
button.grid(row=10, column=1)

#DELETE
label = Label(frame, text="Delete Data")
label.grid(row=8, column=3)

label = Label(frame, text="Delete By Case")
label.grid(row=9, column=3)

id_delete = Entry(frame)
id_delete.grid(row=9, column=4 )

button = Button(frame, text="Delete", command=lambda:delete(id_delete.get()))
button.grid(row=10, column=4)

a = 'abra'
b = 'cad'
print('{0:<5}{1:^5}{0:>5}'.format(a, b))

display_table_casos()

root.mainloop()



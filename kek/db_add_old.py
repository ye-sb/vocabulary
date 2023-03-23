from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import ttk


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
def insert():
    name=ename.get()
    translate=etranslate.get()
    opisanie=eopisanie.get()
    
    if(name=="" or translate=="" or opisanie==""):
        MessageBox.showinfo("Insert status","Все поля со * должны быть заполнены")
    else:
        #con= mysql.connect(host="localhost", user="root", password="root", database="vocabulary", port="3316")
        con= mysql.connect(host="sql8.freesqldatabase.com", user="sql8607007", password="mn1LwmitF7", database="sql8607007", port="3306")      
        insert_vocabulary = "INSERT INTO `terms`(`idbook`, `name`, `translate`, `opisanie`) VALUES ('1','{name}','{translate}','{opisanie}')".format(name=name,translate=translate,opisanie=opisanie)
        execute_query(con, insert_vocabulary)
        
        

window =Tk()
window.geometry('900x1000')
window.title("Добавление терминов")

name=Label(window,text="Термин*")# Сам текст термин
name.place(relx=0.07, rely=0.1, anchor=S)# положение 
ename = Entry()# поле ввода
ename.place(relx=0.2, rely=0.1, anchor=S)# положение

translate=Label(window,text="Перевод на русский*")
translate.place(relx=0.1, rely=0.2, anchor=S)
etranslate = Entry()
etranslate.place(relx=0.25, rely=0.2, anchor=S)

opisanie=Label(window,text="Описание термина*")
opisanie.place(relx=0.1, rely=0.3, anchor=S)
eopisanie = Entry()
eopisanie.place(relx=0.25, rely=0.3, anchor=S)


days=['1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2']
# Определить кортеж дней

# Создайте виджет со списком
var = StringVar()
combobox = ttk.Combobox(window, textvariable = var)
combobox['values'] = days
combobox['state'] = 'readonly'
combobox.pack(fill='x',padx= 3, pady=3)

insert = Button(window, text="Добавить термин", command=insert)
insert.place(relx=0.1,rely=0.5, anchor=S)


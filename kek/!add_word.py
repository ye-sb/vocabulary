from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import ttk
window =Tk()
window.geometry('900x400')
window.title("Добавление терминов")
window.configure(bg="white")
window.resizable(False,False)

#con= mysql.connect(host="localhost", user="root", password="root", database="vocabulary", port="3316")
con= mysql.connect(host="sql8.freesqldatabase.com", user="sql8607007", password="mn1LwmitF7", database="sql8607007", port="3306")      
canvas = Canvas(window,width=890,height=200,bg="white", borderwidth=2, relief="groove")
canvas.place(relx=0, rely=0.4, anchor=W)
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def insert():
    name=str.upper(ename.get())
    translate=str.upper(etranslate.get())
    opisanie=str.upper(eopisanie.get())
    vocabular = var.get()
    
    if(name=="" or translate=="" or opisanie==""):
        MessageBox.showinfo("Insert status","Все поля со * должны быть заполнены")
    else:
        ch=0
        select_double="SELECT COUNT(*) from `terms` where `name`='{name}'".format(name=name)
        result = execute_read_query(con, select_double)
        result=str(result)
        for i in range(len(result)):
            if(result[i]=="0"):
                ch+=1
                break
            
        if(ch==1):
            insert_vocabulary = "INSERT INTO `terms`(`idbook`, `name`, `translate`, `opisanie`) VALUES ((select `id` from `books` where `bname`='{vocabular}'),'{name}','{translate}','{opisanie}')".format(vocabular=vocabular,name=name,translate=translate,opisanie=opisanie)
            execute_query(con, insert_vocabulary)
            MessageBox.showinfo("Insert status","Слово добавлено в словарь")
        else:
            MessageBox.showinfo("Insert status","Такое слово уже есть в словарях")
        
def clean(ename, etranslate, eopisanie):
    ename.delete("0",END)
    etranslate.delete("0",END)
    eopisanie.delete("0",END)

select_terms = "SELECT `bname` from `books` "
terms = execute_read_query(con, select_terms)
option=[None]*(len(terms))
for row in range(0,len(terms)):
    option[row]=terms[row]

var = StringVar()
combobox = ttk.Combobox(window, textvariable = var, font=('Cormorant Infant',16))
combobox['values'] = option
combobox['state'] = 'readonly'
combobox.pack(fill='x',padx= 3, pady=3)

name=Label(window,font=('Cormorant Infant',16), bg="white",text="Термин*")# Сам текст термин
name.place(relx=0.1, rely=0.27, anchor=S)# положение 
ename = Entry(font=('Cormorant Infant',16), relief="flat")# поле ввода
ename.place(relx=0.3, rely=0.27, anchor=S)# положение

translate=Label(window,font=('Cormorant Infant',16),text="Перевод на русский*", bg="white")
translate.place(relx=0.16, rely=0.38, anchor=S)
etranslate = Entry(font=('Cormorant Infant',16),bg="white",relief="flat")
etranslate.place(relx=0.40, rely=0.38, anchor=S)

opisanie=Label(window,font=('Cormorant Infant',16),text="Описание*",bg="white")
opisanie.place(relx=0.11, rely=0.49, anchor=S)
eopisanie = Entry(font=('Cormorant Infant',16), width=50 , relief="flat")
eopisanie.place(relx=0.50, rely=0.49, anchor=S)

cleans = Button(window, font=('Cormorant Infant',15), bg="white",text="ОЧИСТИТЬ", command=lambda: clean(ename, etranslate, eopisanie))
cleans.place(relx=0.1,rely=0.8, anchor=S)

canvas.create_line(160, 52, 380, 52)
canvas.create_line(250, 97, 475, 97)
canvas.create_line(170, 140, 720, 140)
insert = Button(window, font=('Cormorant Infant',16),bg="white", text="Добавить термин",command=insert)
insert.place(relx=0.5,rely=0.85, anchor=S)
















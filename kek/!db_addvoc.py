from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import ttk


con= mysql.connect(host="sql8.freesqldatabase.com", user="sql8607007", password="mn1LwmitF7", database="sql8607007", port="3306")

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
    name=ename.get()
    if(name==""):
        MessageBox.showinfo("Error","Все поля со * должны быть заполнены")
    else:
        ch=0
        #con= mysql.connect(host="localhost", user="root", password="root", database="vocabulary", port="3316")
        select_double="SELECT COUNT(*) from `books` where `bname`='{name}'".format(name=name)
        result = execute_read_query(con, select_double)
        result=str(result)
        for i in range(len(result)):
            if(result[i]=="0"):
                ch+=1
                break
            
        if(ch==1):
            insert_vocabulary = "INSERT INTO `books`(`bname`) VALUES ('{name}')".format(name=name)
            execute_query(con, insert_vocabulary)
            MessageBox.showinfo("","Готово")
        else:  MessageBox.showinfo("","Такой словарь уже есть")
        
            
        
        

window =Tk()
window.geometry('400x400')
window.title("Добавление словарей")
window.configure(bg='white')
window.resizable(False, False)


name=Label(window,text="Название словаря: ",bg="white",font=('Cormorant Infant',16))# Сам текст термин
name.place(relx=0.5, rely=0.3, anchor=S)# положение 
ename = Entry(font=('Cormorant Infant',16),width=29, borderwidth=1,bg="white", relief="groove", justify=CENTER)# поле ввода
ename.place(relx=0.5, rely=0.45, anchor=S)# положение


'''
# Определить кортеж дней
days= ('1','2','3','4','5','6','7')

# Создайте виджет со списком
var = StringVar()
combobox = ttk.Combobox(window, textvariable = var)
combobox['values'] = days
combobox['state'] = 'readonly'
combobox.pack(fill='x',padx= 5, pady=5)
'''

insert = Button(window, text="Добавить словарь",font=('Cormorant Infant',16), bg="white", command=insert)
insert.place(relx=0.5, rely=0.6, anchor=CENTER)

window.mainloop()

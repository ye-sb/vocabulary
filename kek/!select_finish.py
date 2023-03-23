from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import ttk
window =Tk()
window.geometry('900x500')
window.title("Вывод словарей")
window.configure(bg='white')
window.resizable(False, False)

description = Label(window,text="Описание: ")

#con= mysql.connect(host="localhost", user="root", password="root", database="vocabulary", port="3316")
con= mysql.connect(host="sql8.freesqldatabase.com", user="sql8607007", password="mn1LwmitF7", database="sql8607007", port="3306")      
                
#функция чтения из бд
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
#очищение полей        
def clean(ename,text,descrip):
    ename.delete(0,END)
    text['text']=" "
    descrip.delete("1.0","end")
    cleans['state']="disabled"
    c2['state']="disabled"
    var.set(0)

#функция переводчика    
def select():
      name=str.upper(ename.get())
      vocabular = var.get()
      print(vocabular)
      if(name==""):
          MessageBox.showinfo("Insert status","Поле ввода не может быть пустым")
      #какая кнопка включена 
      else:
          
          #con= mysql.connect(host="localhost", user="root", password="root", database="vocabulary", port="3316")
          con= mysql.connect(host="sql8.freesqldatabase.com", user="sql8607007", password="mn1LwmitF7", database="sql8607007", port="3306")      
          select_terms = "SELECT `translate` from `terms` where  `name`='{name}' ".format(vocabular=vocabular,name=name)
          terms = execute_read_query(con, select_terms)
          print(terms)
          if (terms!=None):

              text['text']= terms
              select_terms = "SELECT `opisanie` from `terms` where `name`='{name}'".format(name=name)
              if(var.get()==1):
                  terms = execute_read_query(con, select_terms)
                  descrip.delete("1.0","end")
                  descrip.insert(END,terms)
              if(var.get()==0):
                  descrip.delete("1.0","end")
          
          else:
              var.set(1)
              descrip['state']="normal"
              select_on_text = "SELECT `name` FROM `terms` WHERE `opisanie` like '%{name}%'".format(name=name)
              terms = execute_read_query(con, select_on_text)
             
              for i in range(0,len(terms),1):
                  descrip.insert(END,"\n")
                  descrip.insert(END,terms[i])
              #text.place(relx=0.95, rely=0.4, anchor=E)
              
      cleans['state']="normal"
      c2['state']="normal"
      descrip['state']="normal"
        

def checked(var,descri,name):
    
    if(var.get()==1):
          
        select_terms = "SELECT `opisanie` from `terms` where `name`='{name}'".format(name=name)
        terms = execute_read_query(con, select_terms)
        descrip.insert(END,terms)
        return descrip
    if(var.get()==0): descri.delete("1.0","end")
           
canvas = Canvas(window,width=890,height=200,bg="white", borderwidth=2, relief="groove")
canvas.place(relx=0, rely=0.4, anchor=W)

language1 = Label(window,font=('Cormorant Infant',20),text="АНГЛИЙСКИЙ", bg="white")
language1.place(relx=0.15, rely=0.09)
'''
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
'''


language2 = Label(window,font=('Cormorant Infant',20),text="РУССКИЙ", bg="white")
language2.place(relx=0.7, rely=0.09)

#ввод слова
ename = Entry(window,font=('Cormorant Infant',16),width=29, borderwidth=1,bg="white", relief="flat", justify=CENTER)# поле ввода
ename.place(relx=0.05, rely=0.4, anchor=W)# положение

canvas.create_line(40, 122, 375, 122)
canvas.create_line(550, 122, 850, 122)

descrip=Text(window)
var = IntVar()

c2 = Checkbutton(window, state='disabled', text="Описание",bg="white",font=('Cormorant Infant',16),variable=var,onvalue=1, offvalue=0, command=lambda: checked(var,descrip,ename.get()))
c2.pack(anchor=W, padx=10)
          
text = Label(window,font=('Cormorant Infant',16),text="",justify=CENTER, width=25, height=1, bg="white")
text.place(relx=0.95, rely=0.4, anchor=E)
descrip = Text(window,font=('Cormorant Infant',16),bg="white", width=80, height=5, wrap="word")
descrip.insert(END," ")
descrip.place(relx = 0.5, rely = 0.8, anchor=CENTER)
descrip['state']="disabled"

#кнопка перевести
insert = Button(window, font=('Cormorant Infant',16), text="НАЙТИ", bg="white",command=select)# поменять стиль
insert.place(relx=0.5, rely=0.35, anchor=CENTER)

cleans = Button(window, font=('Cormorant Infant',15), bg="white",text="ОЧИСТКА", command=lambda: clean(ename,text,descrip), state="disabled")
cleans.place(relx=0.5,rely=0.5, anchor=CENTER)


'''
нужно починить кнопку типо после очищения она должна быть дизаблед но потом она начинает шалить
сделать красиво вывод описания
проверка по тексту
'''


   
window.mainloop()        



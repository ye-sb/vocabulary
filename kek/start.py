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

def add_vocabulary():

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
                ename.delete(0,END)
            else:  MessageBox.showinfo("","Такой словарь уже есть")
            
    window_add_vocabulary =Toplevel()
    window_add_vocabulary.geometry('400x400')
    window_add_vocabulary.title("Добавление словарей")
    window_add_vocabulary.configure(bg='white')
    window_add_vocabulary.resizable(False, False)
    window_add_vocabulary.grab_set()
    
    name=Label(window_add_vocabulary,text="Название словаря: ",bg="white",font=('Cormorant Infant',16))# Сам текст термин
    name.place(relx=0.5, rely=0.3, anchor=S)# положение 
    ename = Entry(window_add_vocabulary,font=('Cormorant Infant',16),width=29, borderwidth=1,bg="white", relief="groove", justify=CENTER)# поле ввода
    ename.place(relx=0.5, rely=0.45, anchor=S)# положение
    insert = Button(window_add_vocabulary, text="Добавить словарь",font=('Cormorant Infant',16), bg="white", command=insert)
    insert.place(relx=0.5, rely=0.6, anchor=CENTER)
    window_add_vocabulary.mainloop()
    
def add_termins():
    window_add_termins =Toplevel()
    window_add_termins.geometry('900x400')
    window_add_termins.title("Добавление терминов")
    window_add_termins.configure(bg='white')
    window_add_termins.resizable(False, False)
    window_add_termins.grab_set()
    canvas = Canvas(window_add_termins,width=890,height=200,bg="white", borderwidth=2, relief="groove")
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
    combobox = ttk.Combobox(window_add_termins, textvariable = var, font=('Cormorant Infant',16))
    combobox['values'] = option
    combobox['state'] = 'readonly'
    combobox.pack(fill='x',padx= 3, pady=3)

    name=Label(window_add_termins,font=('Cormorant Infant',16), bg="white",text="Термин*")# Сам текст термин
    name.place(relx=0.1, rely=0.27, anchor=S)# положение 
    ename = Entry(window_add_termins,font=('Cormorant Infant',16), relief="flat")# поле ввода
    ename.place(relx=0.3, rely=0.27, anchor=S)# положение

    translate=Label(window_add_termins,font=('Cormorant Infant',16),text="Перевод на русский*", bg="white")
    translate.place(relx=0.16, rely=0.38, anchor=S)
    etranslate = Entry(window_add_termins,font=('Cormorant Infant',16),bg="white",relief="flat")
    etranslate.place(relx=0.40, rely=0.38, anchor=S)

    opisanie=Label(window_add_termins,font=('Cormorant Infant',16),text="Описание*",bg="white")
    opisanie.place(relx=0.11, rely=0.49, anchor=S)
    eopisanie = Entry(window_add_termins,font=('Cormorant Infant',16), width=50 , relief="flat")
    eopisanie.place(relx=0.50, rely=0.49, anchor=S)

    cleans = Button(window_add_termins, font=('Cormorant Infant',15), bg="white",text="ОЧИСТИТЬ", command=lambda: clean(ename, etranslate, eopisanie))
    cleans.place(relx=0.1,rely=0.8, anchor=S)

    canvas.create_line(160, 52, 380, 52)
    canvas.create_line(250, 97, 475, 97)
    canvas.create_line(170, 140, 720, 140)
    insert = Button(window_add_termins, font=('Cormorant Infant',16),bg="white", text="Добавить термин",command=insert)
    insert.place(relx=0.5,rely=0.85, anchor=S)
    window_add_termins.mainloop()


def search_termins():
    window_search =Toplevel()
    window_search.geometry('900x500')
    window_search.title("Поиск")
    window_search.configure(bg='white')
    window_search.resizable(False, False)
    window_search.grab_set()

    description = Label(window,text="Описание: ")

    #con= mysql.connect(host="localhost", user="root", password="root", database="vocabulary", port="3316")
    #con= mysql.connect(host="sql8.freesqldatabase.com", user="sql8607007", password="mn1LwmitF7", database="sql8607007", port="3306")      
                    
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
          
          if(name==""):
              MessageBox.showinfo("Insert status","Поле ввода не может быть пустым")
          #какая кнопка включена 
          else:
              
              #con= mysql.connect(host="localhost", user="root", password="root", database="vocabulary", port="3316")
              #con= mysql.connect(host="sql8.freesqldatabase.com", user="sql8607007", password="mn1LwmitF7", database="sql8607007", port="3306")      
              select_terms = "SELECT `translate` from `terms` where  `name`='{name}' ".format(vocabular=vocabular,name=name)
              terms = execute_read_query(con, select_terms)
              
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
               
    canvas = Canvas(window_search,width=890,height=200,bg="white", borderwidth=2, relief="groove")
    canvas.place(relx=0, rely=0.4, anchor=W)

    language1 = Label(window_search,font=('Cormorant Infant',20),text="АНГЛИЙСКИЙ", bg="white")
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


    language2 = Label(window_search,font=('Cormorant Infant',20),text="РУССКИЙ", bg="white")
    language2.place(relx=0.7, rely=0.09)

    #ввод слова
    ename = Entry(window_search,font=('Cormorant Infant',16),width=29, borderwidth=1,bg="white", relief="flat", justify=CENTER)# поле ввода
    ename.place(relx=0.05, rely=0.4, anchor=W)# положение

    canvas.create_line(40, 122, 375, 122)
    canvas.create_line(550, 122, 850, 122)

    descrip=Text(window_search)
    var = IntVar()

    c2 = Checkbutton(window_search, state='disabled', text="Описание",bg="white",font=('Cormorant Infant',16),variable=var,onvalue=1, offvalue=0, command=lambda: checked(var,descrip,ename.get()))
    c2.pack(anchor=W, padx=10)
              
    text = Label(window_search,font=('Cormorant Infant',16),text="",justify=CENTER, width=25, height=1, bg="white")
    text.place(relx=0.95, rely=0.4, anchor=E)
    descrip = Text(window_search,font=('Cormorant Infant',16),bg="white", width=80, height=5, wrap="word")
    descrip.insert(END," ")
    descrip.place(relx = 0.5, rely = 0.8, anchor=CENTER)
    descrip['state']="disabled"

    #кнопка перевести
    insert = Button(window_search, font=('Cormorant Infant',16), text="НАЙТИ", bg="white",command=select)# поменять стиль
    insert.place(relx=0.5, rely=0.35, anchor=CENTER)

    cleans = Button(window_search, font=('Cormorant Infant',15), bg="white",text="ОЧИСТКА", command=lambda: clean(ename,text,descrip), state="disabled")
    cleans.place(relx=0.5,rely=0.5, anchor=CENTER)

    window_search.mainloop()
    
window =Tk()
window.geometry('200x200')
window.title("Словари")
window.configure(bg="white")
window.resizable(False,False)


add_voc = Button(text="Создать словарь",command=add_vocabulary)# slovar
add_voc.place(relx=0.1, rely=0.1)

add_terms = Button(text="Добавить термины", command=add_termins)#add terms
add_terms.place(relx=0.1, rely=0.3)

searchb = Button(text="Поиск", command=search_termins)
searchb.place(relx=0.1, rely=0.5)

edit = Button(text="Редактировать")
edit.place(relx=0.1, rely=0.7)




window.mainloop()

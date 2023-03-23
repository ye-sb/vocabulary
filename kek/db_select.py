from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
window =Tk()
window.geometry('900x1000')
window.title("Вывод словарей")

con= mysql.connect(host="localhost", user="root", password="root", database="autocatalog", port="3316")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        
def clicked(id_ca,con):
      new_window = Toplevel(window)
      new_window.title(id_ca)  
      new_window.geometry('500x500')
      
      select_cars = "SELECT car.id_pas,`marka`,`model`,car.gosnomer,`vin`,`type_car`,`type_cat`,`power`,`photo` FROM `car` inner join `pasport` on car.id_pas=pasport.id_pasport where `id_car`='{id_ca}'".format(id_ca=id_ca)
      cars = execute_read_query(con, select_cars)
      
      
      text=Text(new_window, width=50, height=50, font=('Times New Roman',10))
      text.grid(row=0, column=0)
      text.insert(END,cars)
      text.insert(END,'\n')



      
        
select_users = "SELECT `marka`,`model`,pasport.gosnomer,pasport.year_car, `id_car` FROM `car` inner join `pasport` on car.id_pas=pasport.id_pasport"
cars = execute_read_query(con, select_users)
header=['Марка','Модель','Госномер','Год выпуска','№ объявления']

sidecolumn=0
for row in range(len(cars)):
    
    text = Text(width=50, height=10, font=('Open Sans Condensed Light', 20))
    text.grid(row=0, column=sidecolumn)
    
    btn_params_id_car=cars[row][4]
    btn_full_anketa = Button(window,width=20, height=0 , text="Редактировать...", command=lambda: clicked(btn_params_id_car,con))  
    btn_full_anketa.grid(row=0, column=sidecolumn)
    
    
    for column in range(0,5,1):
        #e = Label(window, width=10, fg='blue', text=cars[row][column], anchor=CENTER)
        
        #e.grid(row=(row+1), column=(column+1), pady=5)
        print(header[column],': ' ,cars[row][column], end='\n')
        '''
        headers = Label(window, width=10, fg='red', text=header[column])
        headers.grid(row=column)
        e = Label(window, width=10, fg='blue', text=(cars[row]), anchor=CENTER)
        e.grid(row=(column), column=1, pady=10)
        '''
       # img = PhotoImage(file='bcg.png')
        text.insert(END,header[column])
        text.insert(END, " ")
        text.insert(END, cars[row][column])
        text.insert(END,'\n')
        
        
        
    sidecolumn=sidecolumn+1



  
'''
Уточнить, как сделать вывод как в консоли, только в окне, так как двумерный массив в лейбл не выводится
виджет текст меня не устраивает, либо найти атрибут который запрещает редактироват текст в виджете ТЕКСТ

Идея следующая: в цикле вывод краткой информации по авто, и при нажатии кнопки на конкретной анкете будет открываться окн с полным описанием авто.  в кнопке будет передаваться id машины
запрос есть в блокноте .Либо если я не смогу этого сделать, то просто в цикл выше кину все данные и сделаю кнопку избранное 
'''


   
        



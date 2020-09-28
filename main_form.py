import os 
import sys
import tkinter
from tkinter import *
from tkinter import messagebox
import datetime
import time
from datetime import  date
from datetime import  datetime
import calendar 



root = Tk()
root.geometry("550x175+300+150")
root.title("Ingrese Datos")
root.resizable(width=True, height=True)

##FORM##
lblDate = Label(text="Fecha Actual:",font=("Arial", 14)).place(x=5, y=10)
inDate = StringVar()
txtDate = Entry(root, textvariable=inDate).place(x=200, y=15)

lblhour = Label(text="Hora Actual:",font=("Arial", 14)).place(x=5, y=50)
inHour = StringVar()
txtHour = Entry(root, textvariable=inHour).place(x=200, y=50)

lblBoard = Label(text="Ingrese la Placa:",font=("Arial", 14)).place(x=5, y=80)
inBoard = StringVar()
txtBoard = Entry(root, textvariable=inBoard).place(x=200, y=85)



def board_number ():
    root = Tk()
    root.geometry("500x200+300+150")
    root.title("Resultados")
    root.resizable(width=True, height=True)
    ##obtener fecha##
    stringDate = inDate.get()
    convDate = datetime.strptime(stringDate, '%d/%m/%Y')
    dayWeek = convDate.isocalendar() #obtener dia de la semana 
    ##obtener hora
    digit_Hour = inHour.get()
    convHour = datetime.strptime( digit_Hour , '%H:%M') 
    hourBoardam1 = datetime.strptime("7:30", '%H:%M') 
    hourBoardam2 = datetime.strptime("9:30", '%H:%M') 
    hourBoardpm1 = datetime.strptime("16:00", '%H:%M') 
    hourBoardpm2 = datetime.strptime("19:30", '%H:%M') 
    ##obtener ultimo digito de la placa
    digit = inBoard.get()
    number_digit =  int( (digit[-1]) )
    item_list = 0
    dayList = []
    del dayList [:]
    
    if((number_digit == 1 or number_digit == 2) and dayWeek [2] == 1 and ( convHour <= hourBoardam1 or convHour >=hourBoardpm2 or hourBoardam2<= convHour <= hourBoardpm1) ):
        dayList.append("LUNES: SU COCHE SI PUEDE CIRCULAR")
    else:
        dayList.append("LUNES: SU COCHE NO PUEDE CIRCULAR")



    if ((number_digit == 3 or number_digit == 4) and dayWeek[2] == 2 and ( convHour <= hourBoardam1 or convHour >=hourBoardpm2 or hourBoardam2<= convHour <= hourBoardpm1)):
        dayList.append("MARTES: SI PUEDE CIRCULAR")
    else:  
        dayList.append("MARTES:SU COCHE NO PUEDE CIRCULAR")



    if ((number_digit == 5 or number_digit == 6) and dayWeek[2] == 3 and ( convHour <= hourBoardam1 or convHour >=hourBoardpm2 or hourBoardam2<= convHour <= hourBoardpm1) ):
        dayList.append("MIERCOLES: SI PUEDE CIRCULAR")
    else: 
        dayList.append("MIERCOLES: SU COCHE NO PUEDE CIRCULAR")

    if ((number_digit == 7 or number_digit == 8) and dayWeek[2] == 4 and ( convHour <= hourBoardam1 or convHour >=hourBoardpm2 or hourBoardam2<= convHour <= hourBoardpm1)):
        dayList.append("JUEVES: SI PUEDE CIRCULAR")
    else: 
        dayList.append("JUEVES: SU COCHE NO PUEDE CIRCULAR")

    if ((number_digit == 9 or number_digit == 0) and dayWeek[2] == 5 and ( convHour <= hourBoardam1 or convHour >=hourBoardpm2 or hourBoardam2<= convHour <= hourBoardpm1)):
        dayList.append("VIERNES: SI PUEDE CIRCULAR")
    else: 
        dayList.append("VIERNES: SU COCHE NO PUEDE CIRCULAR")

    if ( number_digit in range (0,9)  and dayWeek[2] == 6 and ( convHour <= hourBoardam1 or convHour >=hourBoardpm2 or hourBoardam2<= convHour <= hourBoardpm1)):
        dayList.append("SÁBADO: SI PUEDE CIRCULAR")
    if ( number_digit in range (0,9)  and dayWeek[2] == 7 and ( convHour <= hourBoardam1 or convHour >=hourBoardpm2 or hourBoardam2<= convHour <= hourBoardpm1)):
        dayList.append("DOMINGO: SI PUEDE CIRCULAR")
    boardList = Listbox (root, width = 70)
    
    for item in dayList:
        print ("item_lst", item_list )
        boardList.insert (item_list, item)
        item_list += 1

    boardList.place(x= 5, y = 15)

   
#####button#####
bntRead = Button(root, padx=5, pady=5, width=43, bg='white', fg='black', relief=GROOVE, command= board_number, text='Consultar', font=('helvetica 15 bold'))
bntRead.place(x=5, y=110)
#############
root.mainloop()
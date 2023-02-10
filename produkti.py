import sqlite3 as sq
import random 
from  tkinter import *
from tkinter.ttk import Combobox

#Datu bāzes iztradāšana un tabulu izveidošana 
try:
    sqlite_connection = sq.connect('veikala_databaze.db')
    sqlite_create_table_klients = '''CREATE TABLE IF NOT EXISTS klients (
        vards TEXT,
        uzvards TEXT,
        presonas_kods TEXT,
        numurs INTEGER,
        sakuma_datums TEXT,
        beidzuma_datums TEXT,
        klientu_id INTERGER);'''
    sqlite_create_table_produtki = '''CREATE TABLE IF NOT EXISTS produkts(
        nosaukums TEXT,
        kategorija TEXT,
        tehniski_raksturojums TEXT,
        pieejams INTEGER,
        cena REAL,
        instrumenti_id INTEGER);'''
    cursor = sqlite_connection.cursor()
    print('Data base is connected')
    cursor.execute(sqlite_create_table_klients)
    sqlite_connection.commit()
    print('Table "klients" is created')
    cursor.execute(sqlite_create_table_produtki)
    sqlite_connection.commit()
    print('Table "produkts" is created')
except sq.Error as error:
    print("Error to conection sqlite base", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Connection to base is closed")

#Aplikacija izmēri
root = Tk()
root.title('Administratora aplikacija')
root.geometry('220x250')

def klientu_registresana():
    window_klient = Tk()
    window_klient.title('Klientu reģistrēšana')
    window_klient.geometry('150x400')

    Label(window_klient, text='Vārds').grid(column=0, row=0 )
    Entry(window_klient, width=15).grid(column=0, row=1) 

    Label(window_klient, text='Uzvārds').grid(column=0, row=2)
    Entry(window_klient, width=15).grid(column=0, row=3) 

    Label(window_klient, text='Personas kods').grid(column=0, row=4)
    Entry(window_klient, width=15).grid(column=0, row=5)

    Label(window_klient, text='Telefona numurs').grid(column=0, row=6 )
    Entry(window_klient, width=15).grid(column=0, row=7)
    Label(window_klient, text='').grid(column=0, row=8)

    Label(window_klient, text='Sākuma datums').grid(column=0, row=9)
    Label(window_klient, text='DD.MM.YYYY').grid(column=0, row=10)
    Entry(window_klient, width=15).grid(column=0, row=11)
    Label(window_klient, text='').grid(column=0, row=12)

    Label(window_klient, text='Beiguma datums').grid(column=0, row=13)
    Label(window_klient, text='DD.MM.YYYY').grid(column=0, row=14)
    Entry(window_klient, width=15).grid(column=0, row=15)

    Button(window_klient, text='Saglabāt')

#Pirmo logu ar pogiem
Label(root, text='').grid(padx=50, pady=1)
Label(root, text='Izvēlēties logu').grid(padx=50, pady=1)
Button(root, text='Klientu reģistrēšana', bg='#94D16C', command=klientu_registresana).grid(padx=50, pady=1)
Button(root, text='Administratora panelis', bg='#F6B662').grid(padx=50, pady=2)
Button(root, text='Exit',bg='#D86874', command=root.destroy).grid(padx=50, pady=3)

root.mainloop()

#https://coderslegacy.com/python/list-of-tkinter-widgets/
#https://www.geeksforgeeks.org/python-gui-tkinter/
#https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter
#https://metanit.com/python/tkinter/4.4.php
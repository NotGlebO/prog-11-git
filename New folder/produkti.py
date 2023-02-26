

import sqlite3 as sq
import random 
from  tkinter import *
from tkinter.ttk import Combobox
from  tkinter import ttk
import tkinter

#Aplikacija izmēri
root = Tk()
root.title('Administratora aplikacija')
root.geometry('220x250')




#Datu bāzes iztradāšana un tabulu izveidošana 
try:
    sqlite_connection = sq.connect('veikala_databaze.db')
    sqlite_create_table_klients = '''CREATE TABLE IF NOT EXISTS klients (
        klientu_id INTEGER,
        vards TEXT,
        uzvards TEXT,
        presonas_kods TEXT,
        numurs TEXT,
        numura_kods TEXT,
        sakuma_datums TEXT,
        beidzuma_datums TEXT);'''
    sqlite_create_table_produtki = '''CREATE TABLE IF NOT EXISTS produkts(
        nosaukums TEXT,
        kategorija TEXT,
        tehniski_raksturojums TEXT,
        pieejams INTEGER,
        cena REAL,
        instruments_id INTEGER);'''

    sqlite_create_table_account = '''CREATE TABLE IF NOT EXISTS personals(
        vards TEXT,
        uzvards TEXT,
        login TEXT,
        password TEXT,
        prefix TEXT);
    '''
    
    cursor = sqlite_connection.cursor()
    Label(root, text='Data base is connected', bg='green').grid(padx=50, pady=5)
    cursor.execute(sqlite_create_table_klients)
    cursor.execute(sqlite_create_table_produtki)
    cursor.execute(sqlite_create_table_account)
    sqlite_connection.commit()
except sq.Error as error:
    Label(root, error, text=" Error to conection sqlite base", bg='Red').grid(padx=50, pady=5)



 
    


#Administratora panelis 
def administratora_panelis():

    admin_window = Tk()
    admin_window.title('Administratora panelis')
    admin_window.geometry('500x500')

    notebook = ttk.Notebook(admin_window)
    notebook.grid(pady=10)
    global frame2
    frame1 = ttk.Frame(notebook, width=500, height=480)
    frame2 = ttk.Frame(notebook, width=500, height=480)
    frame3 = ttk.Frame(notebook, width=500, height=480)
    frame1.grid()
    frame2.grid()
    frame3.grid()
    notebook.add(frame1, text='Instrumenti')
    notebook.add(frame2, text='Administratori')
    notebook.add(frame3, text='Administratoru Tabula')

    
    #Frame 2
    global frame_check_prefix
    frame_add_user = LabelFrame(frame2, text='Add user')
    frame_add_user.grid(column=0, row=0, padx=10)

    frame_check_prefix = LabelFrame(frame2, text='Parbaudīt prefix')
    frame_check_prefix.grid(column=1, row=0, )
    
    
    
    
    
    global users_dict
    users_dict = {}
    for i in cursor.execute('SELECT login, prefix FROM personals'):
        list(i)
        users_dict[i[0]] = [i[1]]

  
    
   

    global combobox_users
    combobox_users = Combobox(frame_check_prefix)
    combobox_users['values'] = [*users_dict.keys()]
    combobox_users['state'] = ['readonly']
    combobox_users.grid(column=3, row=0)
    combobox_users.bind('<<ComboboxSelected>>', users_list_reaction)
    Label(frame_check_prefix, text='Adminstratoru piejamiba: ').grid(column=3, row=1)
    Label(frame_check_prefix, text=' ', font=(35)).grid(column=3,row=4)
    Button(frame_check_prefix, text='Dot prefiksu', command=add_prefix).grid(column=2, row=5)
    Button(frame_check_prefix, text='Atņemt prefiksu', command=remove_prefix).grid(column=3, row=5)


    global user_vards, user_uzvards, user_login, user_parole, user_prefix
    user_vards = Entry(frame_add_user)
    user_uzvards = Entry(frame_add_user)
    user_login = Entry(frame_add_user)
    user_parole = Entry(frame_add_user, show='*')
    user_prefix = Combobox(frame_add_user)
    user_prefix['values'] = ['Jā', 'Nē']
    user_prefix['state'] = ['readonly']
    save_button = Button(frame_add_user, text='Sglābat', command=save_new_user)
   

   
    

    Label(frame_add_user, text='Vārds').grid(column=12,row=19)
    Label(frame_add_user, text='Uzvārds').grid(column=12,row=21)
    Label(frame_add_user, text='Login').grid(column=12,row=23)
    Label(frame_add_user, text='Parole').grid(column=12,row=25)
    Label(frame_add_user, text='Prefix').grid(column=12,row=27)

    user_vards.grid(column=12, row=20)
    user_uzvards.grid(column=12, row=22)
    user_login.grid(column=12, row=24)
    user_parole.grid(column=12, row=26)
    user_prefix.grid(column=12, row=28)
    save_button.grid(column=12, row=32)
    
    columns = ("Vārds", 
    "Uzvārds", 
    "login", 
    'prefix'
    )
    global users_tree
    users_tree = ttk.Treeview(frame3, column=columns, show='headings', height=5)
    users_tree.heading('Vārds', text='Vārds')
    users_tree.heading('Uzvārds', text='Uzvārds')
    users_tree.heading('login', text='Login')
    users_tree.heading('prefix', text='Prefix')

    
    for i in cursor.execute('SELECT vards, uzvards, login, prefix FROM personals'):
        users_tree.insert('', 'end', text="1", values=i)
    
    users_tree.grid()

    Button(frame3, text='Meklēt', command=search_button).grid( padx=100)
    Button(frame3, text='Delete', command=delete).grid(padx=50)

    
    
    
    
    

def search_button():
    search_menu = Tk()
    search_menu.geometry('200x100')
    search_menu.title('Meklēt')
    Entry(search_menu)    
def delete():
    focus_item = users_tree.focus()
    selected_item = users_tree.selection()[0]
    item_details = users_tree.item(focus_item)
    
    users_tree.delete(selected_item)
    cursor.execute(f'DELETE FROM personals WHERE login = "{item_details.get("values")[2]}"') 
    sqlite_connection.commit()

def save_new_user():
    if user_prefix.get() == 'Jā':
        IntPrefix = 1
    else:
        IntPrefix = 0
    sqlite_connection.execute(f'INSERT INTO personals VALUES ("{user_vards.get()}", "{user_uzvards.get()}", "{user_login.get()}", "{user_parole.get()}", {IntPrefix})')
    sqlite_connection.commit()
    users_dict.clear()
    for i in cursor.execute('SELECT login, prefix FROM personals'):
        list(i)
        users_dict[i[0]] = [i[1]]

def add_prefix():
    login = combobox_users.get()
    cursor.execute(f'UPDATE personals SET prefix=1 WHERE login="{login}"')
    sqlite_connection.commit()
    users_dict.clear()
    for i in cursor.execute('SELECT login, prefix FROM personals'):
        list(i)
        users_dict[i[0]] = [i[1]]
    

def remove_prefix():
    login = combobox_users.get()
    cursor.execute(f'UPDATE personals SET prefix=0 WHERE login="{login}"')
    sqlite_connection.commit()
    users_dict.clear()
    for i in cursor.execute('SELECT login, prefix FROM personals'):
        list(i)
        users_dict[i[0]] = [i[1]]

def users_list_reaction(event):
    label_prefix_status_yes = Label(frame_check_prefix, text='Ir pieejams', fg='green', font=('Arial', 15))
    label_prefix_status_no = Label(frame_check_prefix, text='Nav pieejams', fg='red', font=('Arial', 13))
    
    login = event.widget.get()
    prefix = users_dict.get(f'{login}')
    
    if prefix == [1]:
        
        label_prefix_status_yes.grid(column=3,row=4)
        
    else:
        label_prefix_status_no.grid(column=3,row=4)
        
    
    

#Kleintu tabula izveidošna (search)
def klientu_tabula():
    
    

    window_klient.destroy

    main_tk = Tk()

    main_tk.title('Klientu bāze')
    main_tk.geometry('1600x300')
    columns = ('klientu ID',
    "Vārds", 
    "Uzvārds", 
    "Personas kods", 
    'Telefona Numurs',
    'Valstu numura kods',
    'Sakuma datums',
    'Beidzuma datums'
    )
    tree = ttk.Treeview(main_tk, column=columns, show='headings', height=5)
    tree.heading('klientu ID', text='klientu ID')
    tree.heading('Vārds', text='Vārds')
    tree.heading('Uzvārds', text='Uzvārds')
    tree.heading('Personas kods', text='Personas kods')
    tree.heading('Telefona Numurs', text='Telefona Numurs')
    tree.heading('Valstu numura kods', text='Valstu numura kods')
    tree.heading('Sakuma datums', text='Sakuma datums')
    tree.heading('Beidzuma datums', text='Beidzuma datums')
    

    for i in cursor.execute('SELECT * FROM klients'):
        tree.insert('', 'end', text="1", values=i)
    
    

    tree.pack()


#Klientu saglabašana
def saglabasana_datne():
    pedeja_id = len(cursor.execute('SELECT * FROM klients').fetchall())
    try:
        sqlite_connection.execute(f'INSERT INTO klients VALUES ({pedeja_id+1},"{entry_vards.get()}", "{entry_uzvards.get()}", "{entry_personas_kods.get()}", "{entry_telefona_numurs.get()}","{entry_telefona_kods.get()}", "{entry_sakuma_datums.get()}", "{entry_beiguma_datums.get()}")')
        sqlite_connection.commit()
        Label(window_klient, text='Datne saglabojas', fg='green').grid(column=4, row=0)
        Label(window_klient, text=f'Klientu {entry_vards.get()} {entry_uzvards.get()} kods: {pedeja_id+1}', fg='green').grid(column=4, row=1)
    except:
        Label(window_klient, text=f'Error: {sq.Error}', fg='red').grid(column=4, row=0)

#Klientu registrešana
def klientu_registresana():
    global window_klient
    window_klient = Tk()
    window_klient.title('Klientu reģistrēšana')
    window_klient.geometry('400x400')

    global entry_vards
    global entry_uzvards
    global entry_personas_kods
    global entry_telefona_numurs
    global entry_sakuma_datums
    global entry_beiguma_datums
    global entry_telefona_kods

    Label(window_klient, text='Vārds').grid(column=2, row=0 )
    entry_vards = Entry(window_klient, width=15)
    entry_vards.grid(column=2, row=1) 


    Label(window_klient, text='Uzvārds').grid(column=2, row=2)
    entry_uzvards = Entry(window_klient, width=15) 
    entry_uzvards.grid(column=2, row=3)

    Label(window_klient, text='').grid(column=1)

    Label(window_klient, text='Personas kods').grid(column=2, row=4)
    entry_personas_kods = Entry(window_klient, width=15)
    entry_personas_kods.grid(column=2, row=5)

    Label(window_klient, text='Telefona numuru').grid(column=2, row=6 )
    entry_telefona_numurs = Entry(window_klient, width=15)
    entry_telefona_numurs.grid(column=2, row=7)
    

    Label(window_klient, text='Valstu tālruņu kods').grid(column=2, row=9 )
    entry_telefona_kods = Entry(window_klient, width=16)
    entry_telefona_kods.grid(column=2, row=10)
    

    Label(window_klient, text='Sākuma datums').grid(column=2, row=11)
    Label(window_klient, text='DD.MM.YYYY').grid(column=2, row=12)
    entry_sakuma_datums = Entry(window_klient, width=15)
    entry_sakuma_datums.grid(column=2, row=13)
    Label(window_klient, text='').grid(column=2, row=14)

    Label(window_klient, text='Beiguma datums').grid(column=2, row=15)
    Label(window_klient, text='DD.MM.YYYY').grid(column=2, row=16)
    entry_beiguma_datums = Entry(window_klient, width=15)
    entry_beiguma_datums.grid(column=2, row=17)


    Button(window_klient, text='Saglabāt', command=saglabasana_datne).grid(column=1, row=18)
    Button(window_klient, text='Paradīt klientus', command=klientu_tabula).grid(column=2, row=18)
    Button(window_klient, text='Aizslēgt', command=window_klient.destroy).grid(column=3, row=18)


    

#Pirmo logu ar pogiem
Label(root, text='').grid(padx=50, pady=1)
Label(root, text='Izvēlēties logu').grid(padx=50, pady=1)
Button(root, text='Klientu reģistrēšana', bg='#94D16C', command=klientu_registresana,).grid(padx=50, pady=1)
Button(root, text='Administratora panelis', bg='#F6B662', command=administratora_panelis).grid(padx=50, pady=2)
Button(root, text='Exit',bg='#D86874', command=root.destroy).grid(padx=50, pady=3)

root.mainloop()

#https://coderslegacy.com/python/list-of-tkinter-widgets/
#https://www.geeksforgeeks.org/python-gui-tkinter/
#https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter
#https://metanit.com/python/tkinter/4.4.php

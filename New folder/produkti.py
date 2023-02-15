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
    notebook.pack(pady=10, expand=True)
    global frame2
    frame1 = ttk.Frame(notebook, width=500, height=480)
    frame2 = ttk.Frame(notebook, width=500, height=480)
    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)
    notebook.add(frame1, text='1')
    notebook.add(frame2, text='1')


    pozicija = {"padx":6, "pady":6, "anchor":NW}
    checkbutton_klients_table = Checkbutton(frame2, text='Klientu tabula')
    checkbutton_klients_table.pack(**pozicija)

    checkbutton_admin_produkts = Checkbutton(frame2, text='Produktu tabula izmainišana tabula')
    checkbutton_admin_produkts.pack(**pozicija)

    checkbutton_admin_users = Checkbutton(frame2, text='Administratora mainīšana')
    checkbutton_admin_users.pack(**pozicija)

    global combobox_user_value
    combobox_user_value = StringVar()
    combobox_users = Combobox(frame2, textvariable=combobox_user_value)
    combobox_users['values'] = ['test']
    combobox_users['state'] = ['readonly']
    combobox_users.pack(side=LEFT)
    combobox_users.bind('<<ComboboxSelect>>', users_list_reaction)
    

def users_list_reaction(event):
    lists_users = []
    users = cursor.execute(f'SELECT * FROM personals WHERE login = {combobox_user_value.get()}').fetchall() 
    
    for i in users:
        lists_users.append(i)
    print(lists_users)

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
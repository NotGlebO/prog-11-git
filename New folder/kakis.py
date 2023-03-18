

import sqlite3 as sq
from  tkinter import *
from tkinter.ttk import Combobox
from  tkinter import ttk
import hashlib
from tkinter import messagebox





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
    cursor.execute(sqlite_create_table_klients)
    cursor.execute(sqlite_create_table_produtki)
    cursor.execute(sqlite_create_table_account)
    sqlite_connection.commit()

    admin_check = cursor.execute('SELECT login FROM personals WHERE login = "admin"').fetchone()
    ne_admin_check = cursor.execute('SELECT login FROM personals WHERE login = "neadmin"').fetchone()
    

    if admin_check == None:
        
        cursor.execute('INSERT INTO personals VALUES ("admin", "admin", "admin", "21232f297a57a5a743894a0e4a801fc3", "1")')
        sqlite_connection.commit()
    
    if ne_admin_check == None:
        cursor.execute('INSERT INTO personals VALUES ("neadmin", "neadmin", "neadmin", "a969c43e2bd1ff992ef87554cfac4a2f", "0")')
        sqlite_connection.commit()
        
    
except:
    pass

#Pieteikšanās un paroles ievades paneļa izveidošana

def confirm_button():
    global login
    login = cursor.execute(f'SELECT login, password FROM personals WHERE login = "{entry_login.get()}"').fetchall()
    

    if len(login) == 0:
        Label(log_menu, text='Nepareiza logina vai parole', fg='red').grid(column=1, row=3)

    else:
        if hashlib.md5(f'{entry_password.get()}'.encode('UTF-8')).hexdigest() == login[0][1]:
            menu()
        else:
            Label(log_menu, text='Nepareiza logina vai parole', fg='red').grid(column=1, row=3)
        
#Administratora paneļa izveidošana

def administratora_panelis():

    prefix = cursor.execute(f'SELECT prefix FROM personals WHERE login = "{login[0][0]}"').fetchall()
    
    if prefix[0][0] != 1:
        messagebox.showerror('Kļūda', 'Nav Prefiksu')

    else:
        global users_tree, frame2, frame3, search_user_entry, frame_check_prefix, users_dict, combobox_users, instrument_tree

        admin_window = Tk()
        admin_window.title('Administrātora panelis')
        admin_window.geometry('1200x700')

        notebook = ttk.Notebook(admin_window)
        notebook.grid(pady=10)
        
        global frame1
        frame1 = ttk.Frame(notebook, width=500, height=480)
        frame2 = ttk.Frame(notebook, width=500, height=480)
        frame3 = ttk.Frame(notebook, width=500, height=480)
        frame1.grid()
        frame2.grid()
        frame3.grid()
        notebook.add(frame1, text='Instrumenti')
        notebook.add(frame2, text='Administrātori')
        notebook.add(frame3, text='Administrātora tabula')

        #Rāmis 1
        
        instrumen_columns = ("Nosaukums", 
        "Kategorija", 
        "Teh. raksturojums", 
        'Pieejams',
        'Cena',
        'Instrumenta id'
        )
        
        global instrument_tree
        instrument_tree = ttk.Treeview(frame1, column=instrumen_columns, show='headings', height=10)
        instrument_tree.grid(column=0, row=0)
        


        instrument_tree.heading('Nosaukums', text='Nosaukums')
        instrument_tree.heading('Teh. raksturojums', text='Teh. raksturojums')
        instrument_tree.heading('Kategorija', text='Kategorija')
        instrument_tree.heading('Pieejams', text='Pieejamība')
        instrument_tree.heading('Cena', text='Cena')
        instrument_tree.heading('Instrumenta id', text='Instrumenta ID')
        
        for i in cursor.execute('SELECT * FROM produkts'):
            instrument_tree.insert('', 'end', text="1", values=i)
        
        
        global entry_nosaukums, entry_rakturojums, entry_kategorija, entry_pieejams, entry_cena, entry_instrumenta_id
        label_nosaukums = Label(frame1, text='Nosaukums')
        entry_nosaukums = Entry(frame1, width=15)
        label_raksturojums = Label(frame1, text='Raksturojums')
        entry_rakturojums = Text(frame1, width=50, height=10)
        label_kategorija = Label(frame1, text='Kategorija')
        entry_kategorija = Entry(frame1, width=15)
        label_pieejams = Label(frame1, text='Pieejams')
        entry_pieejams = Entry(frame1, width=15)
        label_cena = Label(frame1, text='Cena')
        entry_cena = Entry(frame1)
        label_istrumenta_id = Label(frame1, text='Instrumenta ID')
        entry_instrumenta_id = Entry(frame1)
        instrument_add = Button(frame1, text='Pievienot instrumentu', command=add_instrument)
        instrument_remove = Button(frame1, text='Dzēst instrumentu', command=remove_instrument)

        label_nosaukums.grid()
        entry_nosaukums.grid()
        label_raksturojums.grid()
        entry_rakturojums.grid()
        label_kategorija.grid()
        entry_kategorija.grid()
        label_pieejams.grid()
        entry_pieejams.grid()
        label_cena.grid()
        entry_cena.grid()
        label_istrumenta_id.grid()
        entry_instrumenta_id.grid()
        instrument_add.grid()
        instrument_remove.grid()

        #Rāmis 2

        frame_add_user = LabelFrame(frame2, text='Pievienot lietotāju')
        frame_add_user.grid(column=0, row=0, padx=10)

        frame_check_prefix = LabelFrame(frame2, text='Parbaudīt prefiksu')
        frame_check_prefix.grid(column=1, row=0, )
        
        
        
        
        
        
        users_dict = {}
        for i in cursor.execute('SELECT login, prefix FROM personals'):
            list(i)
            users_dict[i[0]] = [i[1]]

    
        
    

        
        combobox_users = Combobox(frame_check_prefix)
        combobox_users['values'] = [*users_dict.keys()]
        combobox_users['state'] = ['readonly']
        combobox_users.grid(column=3, row=0)
        combobox_users.bind('<<ComboboxSelected>>', users_list_reaction)
        Label(frame_check_prefix, text='Adminstratoru pieejamība: ').grid(column=3, row=1)
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
        save_button = Button(frame_add_user, text='Saglābat', command=save_new_user)
    

    
        

        Label(frame_add_user, text='Vārds').grid(column=12,row=19)
        Label(frame_add_user, text='Uzvārds').grid(column=12,row=21)
        Label(frame_add_user, text='Login').grid(column=12,row=23)
        Label(frame_add_user, text='Parole').grid(column=12,row=25)
        Label(frame_add_user, text='Prefiks').grid(column=12,row=27)

        user_vards.grid(column=12, row=20)
        user_uzvards.grid(column=12, row=22)
        user_login.grid(column=12, row=24)
        user_parole.grid(column=12, row=26)
        user_prefix.grid(column=12, row=28)
        save_button.grid(column=12, row=32)
        
        #Rāmis 3

        columns = ("Vārds", 
        "Uzvārds", 
        "login", 
        'prefix'
        )
        
        users_tree = ttk.Treeview(frame3, column=columns, show='headings', height=5)
        users_tree.heading('Vārds', text='Vārds')
        users_tree.heading('Uzvārds', text='Uzvārds')
        users_tree.heading('login', text='Login')
        users_tree.heading('prefix', text='Prefiks')

        
        for i in cursor.execute('SELECT vards, uzvards, login, prefix FROM personals'):
            users_tree.insert('', 'end', text="1", values=i)
        
        users_tree.grid(column=0, row=0)

        
        frame_search_user = LabelFrame(frame3, text='Pievienot lietotāju')
        frame_search_user.grid(pady=14)

        Label(frame_search_user, text='Uzvārds').grid(padx=2) 
        search_user_entry = Entry(frame_search_user)
        search_user_entry.grid()  
        Button(frame_search_user, text='Meklēt', command=search_button_users).grid(pady=15) 
        
        Button(frame3, text='Dzēst', command=delete_user).grid(padx=50)

    
#Paneļa izveidošana, ar kuru var pievienot instrumentu

def add_instrument():

    sqlite_connection.execute(f'INSERT INTO produkts VALUES ("{entry_nosaukums.get()}", "{entry_kategorija.get()}", "{entry_rakturojums.get("1.0",)}", "{entry_pieejams.get()}", "{entry_cena.get()}", "{entry_instrumenta_id.get()}")')
    sqlite_connection.commit()
    

  
    instrument_tree.insert('', 'end', text="1", values=(entry_nosaukums.get(), entry_kategorija.get(),entry_rakturojums.get("1.0",), entry_pieejams.get(), entry_cena.get(),entry_instrumenta_id.get() ) )

#Paneļa izveidošana, ar kuru var noņemt instrumentu

def remove_instrument():
    focus_item = instrument_tree.focus()
    selected_item = instrument_tree.selection()[0]
    item_details = instrument_tree.item(focus_item)
    
    instrument_tree.delete(selected_item)
    cursor.execute(f'DELETE FROM produkts WHERE instruments_id = "{item_details.get("values")[5]}"') 
    sqlite_connection.commit()

#Pogu izveidošana, kas ļaus meklēt lietotājus datu bāzē

def search_button_users():

    if search_user_entry.get() == '':
        searched_uzvards = cursor.execute('SELECT vards, uzvards, login, prefix FROM personals')
    else:
        searched_uzvards = cursor.execute(f'SELECT vards, uzvards, login, prefix FROM personals WHERE uzvards LIKE "{search_user_entry.get()}"')
    columns = ("Vārds", 
    "Uzvārds", 
    "login", 
    'prefix'
    )
    
    users_tree = ttk.Treeview(frame3, column=columns, show='headings', height=5)
    users_tree.heading('Vārds', text='Vārds')
    users_tree.heading('Uzvārds', text='Uzvārds')
    users_tree.heading('login', text='Login')
    users_tree.heading('prefix', text='Prefiks')

    
    for i in searched_uzvards:
        users_tree.insert('', 'end', text="1", values=i)
    
    users_tree.grid(column=0, row=0)
     
#Pogu izveidošana, ar kuru var izdzēst lietotāju

def delete_user():
    focus_item = users_tree.focus()
    selected_item = users_tree.selection()[0]
    item_details = users_tree.item(focus_item)
    
    users_tree.delete(selected_item)
    cursor.execute(f'DELETE FROM personals WHERE login = "{item_details.get("values")[2]}"') 
    sqlite_connection.commit()

#Pogu izveidošana, ar kuru varat saglabāt jaunu lietotāju datu bāzē

def save_new_user():
    if user_prefix.get() == 'Jā':
        IntPrefix = 1
    else:
        IntPrefix = 0


    login_prefix = cursor.execute(f'SELECT login FROM personals WHERE login = "{user_login.get()}"').fetchall()
    print(login_prefix)
    if len(login_prefix) == 1:
        messagebox.showerror('Kļūda', 'Ir lietotājs ar šādu loginu')
    else:
        user_parole_md5 = hashlib.md5(f'{user_parole.get()}'.encode('UTF-8')).hexdigest()
        sqlite_connection.execute(f'INSERT INTO personals VALUES ("{user_vards.get()}", "{user_uzvards.get()}", "{user_login.get()}", "{user_parole_md5}", {IntPrefix})')
        sqlite_connection.commit()
        users_dict.clear()
        for i in cursor.execute('SELECT login, prefix FROM personals'):
            list(i)
            users_dict[i[0]] = [i[1]]

#Prefiksa izveide

def add_prefix():
    login = combobox_users.get()
    cursor.execute(f'UPDATE personals SET prefix=1 WHERE login="{login}"')
    sqlite_connection.commit()
    users_dict.clear()
    for i in cursor.execute('SELECT login, prefix FROM personals'):
        list(i)
        users_dict[i[0]] = [i[1]]
    
#Prefiksa noņemšana

def remove_prefix():
    login = combobox_users.get()
    cursor.execute(f'UPDATE personals SET prefix=0 WHERE login="{login}"')
    sqlite_connection.commit()
    users_dict.clear()
    for i in cursor.execute('SELECT login, prefix FROM personals'):
        list(i)
        users_dict[i[0]] = [i[1]]

#Programmas reakcija uz lietotāju sarakstu

def users_list_reaction(event):
    label_prefix_status_yes = Label(frame_check_prefix, text='Ir pieejams', fg='green', font=('Arial', 15))
    label_prefix_status_no = Label(frame_check_prefix, text='Nav pieejams', fg='red', font=('Arial', 13))
    
    login = event.widget.get()
    prefix = users_dict.get(f'{login}')
    
    if prefix == [1]:
        
        label_prefix_status_yes.grid(column=3,row=4)
        
    else:
        label_prefix_status_no.grid(column=3,row=4)
        
#Kleintu tabula izveidošna (meklēšana)

def klientu_tabula():
    
    

    window_klient.destroy
    global main_tk
    main_tk = Tk()

    main_tk.title('Klientu bāze')
    main_tk.geometry('1800x300')
    columns = ('klientu ID',
    "Vārds", 
    "Uzvārds", 
    "Personas kods", 
    'Telefona Numurs',
    'Valstu numura kods',
    'Sakuma datums',
    'Beidzuma datums',
    'Instruments_id'
    )
    global tree
    tree = ttk.Treeview(main_tk, column=columns, show='headings', height=5)
    tree.heading('klientu ID', text='klientu ID')
    tree.heading('Vārds', text='Vārds')
    tree.heading('Uzvārds', text='Uzvārds')
    tree.heading('Personas kods', text='Personas kods')
    tree.heading('Telefona Numurs', text='Telefona numurs')
    tree.heading('Valstu numura kods', text='Valsts telefona kods')
    tree.heading('Sakuma datums', text='Sākuma datums')
    tree.heading('Beidzuma datums', text='Beiguma datums')
    tree.heading('Instruments_id', text='Instrumenta ID')

    for i in cursor.execute('SELECT * FROM klients'):
        tree.insert('', 'end', text="1", values=i)
    
    tree.grid()
    frame_search_klient = LabelFrame(main_tk, text='Pievienot lietotāju')
    frame_search_klient.grid(pady=14)

    global search_klients_entry
    Label(frame_search_klient, text='Uzvārds').grid(padx=2) 
    search_klients_entry = Entry(frame_search_klient)
    search_klients_entry.grid() 

    Button(frame_search_klient, text='Meklēt klientu', command=search_button_klients).grid()
    Button(main_tk, text='Dzēst', command=delete_klients).grid()

#Klientu meklēšanas pogas izveidošana

def search_button_klients():


    if search_klients_entry.get() == '':
        searched_uzvards = cursor.execute('SELECT * FROM klients')
    else:
        searched_uzvards = cursor.execute(f'SELECT * FROM klients WHERE uzvards LIKE "{search_klients_entry.get()}"').fetchall()
        for item in tree.get_children():
            tree.delete(item)
    for i in searched_uzvards:
        tree.insert('', 'end', text="1", values=i)
    
#Klientu saglabāšana

def saglabasana_datne():
 
    pedeja_id = cursor.execute('SELECT klientu_id FROM klients').fetchall()
    if pedeja_id == []:
        pedeja_id = 0
    else:
        for i in max(pedeja_id):
            try:
                pedeja_id = i
            except:
                pass
    try:
        sqlite_connection.execute(f'INSERT INTO klients VALUES ({pedeja_id+1},"{entry_vards.get()}", "{entry_uzvards.get()}", "{entry_personas_kods.get()}", "{entry_telefona_numurs.get()}","{entry_telefona_kods.get()}", "{entry_sakuma_datums.get()}", "{entry_beiguma_datums.get()}", "{entry_instruments_id.get()}")')
        sqlite_connection.commit()
        Label(window_klient, text='Datne saglabājas', fg='green').grid(column=4, row=0)
        Label(window_klient, text=f'Klientu {entry_vards.get()} {entry_uzvards.get()} kods: {pedeja_id+1}', fg='green').grid(column=4, row=1)
    except:
        Label(window_klient, text=f'Kļūda: {sq.Error}', fg='red').grid(column=4, row=0)

#Klientu noņemšana

def delete_klients():

    focus_item = tree.focus()
    selected_item = tree.selection()[0]
    item_details = tree.item(focus_item)
    
    tree.delete(selected_item)
    cursor.execute(f'DELETE FROM klients WHERE klientu_id = "{item_details.get("values")[0]}"') 
    sqlite_connection.commit()

#Klientu reģistrēšana

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
    global entry_instruments_id

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

    Label(window_klient, text='Telefona numurs').grid(column=2, row=6 )
    entry_telefona_numurs = Entry(window_klient, width=15)
    entry_telefona_numurs.grid(column=2, row=7)
    

    Label(window_klient, text='Valsts telefona kods').grid(column=2, row=9 )
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


    Label(window_klient, text='Instrumentu ID').grid(column=3, row=0 )
    entry_instruments_id = Entry(window_klient, width=16)
    entry_instruments_id.grid(column=3, row=1)

    Button(window_klient, text='Saglabāt', command=saglabasana_datne).grid(column=1, row=18)
    Button(window_klient, text='Paradīt klientus', command=klientu_tabula).grid(column=2, row=18)
    Button(window_klient, text='Aizslēgt', command=window_klient.destroy).grid(column=3, row=18)

#Izvēlnes izveidošana
    
def menu():

    log_menu.destroy()
    #Lietojumprogrammas izmēri
    root = Tk()
    root.title('Administrātora aplikacija')
    root.geometry('220x250')
    #Pirmais logs ar pogām
    Label(root, text='').grid(padx=50, pady=1)
    Label(root, text='Izvēlēties logu').grid(padx=50, pady=1)
    Button(root, text='Klientu reģistrēšana', bg='#94D16C', command=klientu_registresana,).grid(padx=50, pady=1)
    Button(root, text='Administrātora panelis', bg='#F6B662', command=administratora_panelis).grid(padx=50, pady=2)
    Button(root, text='Iziet',bg='#D86874', command=root.destroy).grid(padx=50, pady=3)


log_menu = Tk()
log_menu.geometry('220x250')
log_menu.title('Login')
entry_login = Entry(log_menu)
entry_password = Entry(log_menu, show='*')
connect_button = Button(log_menu, text='Apstiprināt', command=confirm_button)

Label(log_menu, text='Login').grid(column=0, row=0)
entry_login.grid(column=1, row=0)
Label(log_menu, text='Parole').grid(column=0, row=1, pady=7)
entry_password.grid(column=1, row=1)
connect_button.grid(column=1, row=2)
log_menu.mainloop()



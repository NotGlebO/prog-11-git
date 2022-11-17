
from tkinter import * 
from tkinter import ttk
import random

# check = random.randrange(1, 999999)
# f = open(f"/Users/gostapko/Desktop/New folder/check/check{check}.txt", "w", encoding="utf-8") 
root = Tk()
#Размеры
root.title('PC')
root.geometry('400x200+700+500')
root.resizable(width=False, height=False)
# class Table:
#     def __init__(self, veids, modelis, cena):
#         self.veids = veids
#         self.modelis = modelis
#         self.cena = cena
#     def check(self):
#         l = ['-Personālā datora sastāvdaļa-\n','Veids: ' + self.veids + "\n", "Modelis: " + self.modelis + "\n" ,"Cena: " + str(self.cena) ]
#         f.writelines(l)

# veids = StringVar() 
# nosaukums = StringVar()
cena = StringVar()

fr = Frame(root)
fr.pack
#Список товаров
vlist = ['RAM', 'CPU', 'GPU']
mlist = ['Corsair Vengeance LPX 16GB', 'Gigabyte GeForce 720 2GB', 'AMD Ryzen 7 5800x 3,8GHz']

#Выбор товаров
vcombo = ttk.Combobox(values=vlist)
vcombo.set('Выберите карту')
vcombo.pack(anchor=NW, padx = 0, pady = 0)

mcombo = ttk.Combobox(values=mlist)
mcombo.set('Выберите карту')
mcombo.pack(anchor=NW, padx = 0, pady = 10)


e = Entry(textvariable=cena).place(x=40, y=70)
cena_choose = Label(root, text= "Cena:").place(x=0, y=70)
#кнопки
update = Button(root, text='Update', command=root.destroy).place(x=20, y=30)
save = Button(root, text='Save', command=root.destroy).place(x=20, y=30)
exit = Button(root, text='Exit', command=root.destroy).place(x=20, y=30)

#Чек в окне
check = Label(root, text= "-Personālā datora sastāvdaļa-").place(x=200, y=3)
veids_check = Label(root, text= "Veids:").place(x=200, y=30)
nosaukums_check = Label(root, text= "Modelis:").place(x=200, y=50)
cena_check = Label(root, text= "Cena:").place(x=200, y=70)
root.mainloop()

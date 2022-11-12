from tkinter import * 
import random

check = random.randrange(1, 999999)
f = open(f"/Users/PC/Desktop/School/prog/check/check{check}.txt", "w", encoding="utf-8") 
root = Tk()

root.title('PC')
root.geometry('400x200+700+500')
root.resizable(width=False, height=False)
class Table:
    def __init__(self, veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    def check(self):
        l = ['-Personālā datora sastāvdaļa-\n','Veids: ' + self.veids + "\n", "Modelis: " + self.modelis + "\n" ,"Cena: " + str(self.cena) ]
        f.writelines(l)

PC = StringVar() 
RAM = Table("RAM", "Corsair Vengeance LPX 16GB", 99.99)
GPU = Table("GPU", "Gigabyte GeForce 720 2GB", 75.50)
CPU = Table("CPU", "AMD Ryzen 7 5800x 3,8GHz", 657.80)

e = Entry(textvariable=PC)
b = Button(text='Ok')

e.pack()
b.pack()

root.mainloop()

if PC.get() == "RAM":
    PC1 = RAM
if PC.get() == "CPU":
    PC1 = CPU
if PC.get() == "GPU":
    PC1 = GPU
PC1.check()
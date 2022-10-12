import sqlite3 as sq

c = sq.connect('/Users/gostapko/Desktop/New folder/k.db')
cur = c.cursor()

kategorija = input('Kategorija: ')
nosaukums = input("nosaukums: ")
rakst = input("Raksturojums: ")
cena = input('Cena: ')
pieejams = bool(input("Pieejams"))
vards = input("Vards: ")
uzvards = input('uzvards: ')
pk = input('pk: ')
numurs= input('Numurs: ')
db = input('datu sākums: ')
sk = input('Datu beigums: ')


class Inst:
    def __init__(sell, piej):
        sell.piej = pieejams
    
    def __init__(self, cat, nos, th, cen):
        self.cat = kategorija
        self.nos = nosaukums
        self.th =  rakst
        self.cen = cena
        

if pieejams == True:
    c.execute(f'INSERT INTO klienti (inst, vards, uzvards, pk, numurs, sdatums, bdatums, rakst, kategorija) VALUES ("{nosaukums}", "{vards}","{uzvards}", "{pk}", "{numurs}", "{sk}", "{db}", "{rakst}", "{kategorija}")')


c.commit()
c.close()
import sqlite3 as sq

c = sq.connect('/Users/PC/Desktop/School/prog/k.db')
cur = c.cursor()

kategorija = input('f')
nosaukums = input("f")
rakst = input(" ")
cena = input('')
pieejams = bool(input())
vards = input()
uzvards = input()
pk = input()
numurs= input()
cena = input()
db = input()
sk = input()


class Inst:
    def __init__(sell, piej):
        sell.piej = pieejams
    
    def __init__(self, cat, nos, th, cen):
        self.cat = kategorija
        self.nos = nosaukums
        self.th =  rakst
        self.cen = cena
        

if pieejams == True:
    cur.execute(f'INSERT INTO klienti (inst, vards, uzvards, pk, numurs, sdatums, bdatums) VALUES ("{nosaukums}", "{vards}","{uzvards}", "{pk}", "{numurs}", "{sk}", "{db}")')


c.commit()
c.close()

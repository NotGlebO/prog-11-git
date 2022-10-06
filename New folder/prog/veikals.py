import sqlite3 as sq
import random 
c = sq.connect('/Users/PC/Desktop/School/prog/k.db')
cur = c.cursor()



pid = int(input("preču ID: "))

name = input("vārds: ")
sname = input("uzvards: ")
pk = input("Jūsu p.k: ")
tnumber = int(input("telefona numurs: "))
sd =input("sākuma datums: ")
bd = input("beigu datums: ")

pid1 = pid - 1

id = random.randrange(1000, 9999)
idk = cur.execute("SELECT idk FROM klienti ")
idk = cur.fetchall()
while id == idk:
    id = random.randrange(1000, 9999)

myresult = cur.execute("SELECT pieejams FROM produki ")
myresult = cur.fetchall()
out = [item for t in myresult for item in t]


pid2 = out[pid1] - 1




cur.execute(f"UPDATE produki SET pieejams = {pid2} WHERE id = {pid}")




    


c.execute(f'INSERT INTO klienti (inst, vards, uzvards, pk, numurs, sdatums, bdatums, idk) VALUES ("{pid}", "{name}","{sname}", "{pk}", "{tnumber}", "{sd}", "{bd}", {id})')


c.commit()
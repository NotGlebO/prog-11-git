import sqlite3 as sq
import random 
import numpy as np
c = sq.connect('/Users/gostapko/Desktop/New folder/k.db')
cur = c.cursor()



pid = int(input("preču ID: "))
'''
name = input("vārds: ")
sname = input("uzvards: ")
pk = input("Jūsu p.k: ")
tnumber = int(input("telefona numurs: "))
sd =input("sākuma datums: ")
bd = input("beigu datums: ")
'''
pid1 = pid - 1

id = random.randrange(1000, 9999)
idk = cur.execute("SELECT idk FROM klienti ")
idk = cur.fetchall()
while id == idk:
    id = random.randrange(1000, 9999)
a = []
myresult = cur.execute("SELECT pieejams FROM produki ")
myresult = list(cur.fetchall())
print(myresult[pid])
for nym in myresult:
    at = myresult[pid] - 1
    print(at)
#print(pida)
#cur.execute(f"UPDATE produki SET pieejams = {pida} WHERE idk = {pid}")




    


#c.execute(f'INSERT INTO klienti (inst, vards, uzvards, pk, numurs, sdatums, bdatums, idk) VALUES ("{pid}", "{name}","{sname}", "{pk}", "{tnumber}", "{sd}", "{bd}", {id})')


c.commit()



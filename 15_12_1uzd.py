print('No 2 preces, būs atlaide')
dz = int(input('Īzveles produktu daudzums '))
summ = dz * 2.35
print(summ)

if dz >= 2:
  print('Jūsu atlaide ir 10%')
  atl = summ *10 / 100
  at = round(summ - atl, 2)
  print('Cena par pirkumiem ir ' + str(at))
else: 
  print('Jūms nav atlaide')

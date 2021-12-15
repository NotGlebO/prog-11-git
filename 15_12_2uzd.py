pr = int(input('Ievadīt pirmo spēlētāju punktu skaists'))
ot = int(input('Ievadīt otro spēlētāju punktu skaits'))

if pr > ot:
  print('Uzvar pirmais')

elif pr == ot:
  print('Ņeizšķirt')


else: 
  print('Uzvar otrais')

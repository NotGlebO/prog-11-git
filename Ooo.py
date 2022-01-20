gordeja = input('Ievadīt tekstu: ')

def ostapko():
  if gordeja.count('o') or gordeja.count('O'):
      shkoda = gordeja.replace('o', '%')
      molotkova = shkoda.replace('O', '%')
      print(molotkova)
  else:
    print('nav O')

ostapko()

e = input('Ievadit text: ')

def deleted(e):
  if e.count('e')>0:
    e = e.replace('e',' ')
    print(e.upper())
  else:
    e = print(' NE KO SEIT NAV')
  return e

deleted(e)

a = input('Ievadit tekss: ')

def replaceDivi(a):
  if a.count("2")>0:
    a = a.replace('2','divi')
    print(a)
  else:
    a = print("Nekas nav")
  return a


replaceDivi(a)

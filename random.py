
a = input('rakstit textu: ')

def reverstiik(a):
  sar1 = a.split()
  if len(sar1)>1:
    sar1.reverse()
    a = '' 
    for elements in sar1:
      a += elements
      print(a)
  else:
    a = print('loti mazak')
  return a

reverstiik(a)

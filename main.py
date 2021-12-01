a = input("Write a list: ")

def countNumbers(rool):
  summa = 0
  for simbols in rool:
    summa = summa + int(simbols)
  return summa

print(countNumbers(a))


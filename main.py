#funcion no recibe ni retorna
def funcion01():
  c = 2 * 6
  print(c)
 

  # funcion con dos parametros

def funcion02(a,b):
  v = a * b
  print(v)


#funcion que no recibe nada, pero retorna dos valores

def funcion03():
  a = 4
  b = 5
  return a, b


funcion01()
funcion02(3 , 7)
gA , gB= funcion03 ()
print (gA)
print (gB)

#funcion con dos parametros y retorna 1 valor
 
def funcion04(a,b):
  v = a * b
  return v

gC = funcion04 (gA,gB)
print (gC)
 
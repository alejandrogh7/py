print(type(4))
print(type('hello'))
print(type(2.5))
print(type(True))
print(type(3 + 5j))


name = str(input('Insert your name >>> '))
print('Hello', name)

#Se fuerza de forma visual pero no lógica :/ Ts > Py
ageStrong: int = 45
# ageStrong = '45' >>>> Error

#Operators
#----Aritmeticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)

print('Hello ' + str(234) + ' World')
print('Hello' * 2)

#----Comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print('----STR----')
'''
Comprueba una ordenación alfabetica
cual está más a la derecha que la otra :/:
'''
print('UNO' < 'TRES')
print('UNO' > 'TRES')
print('UNO' >= 'TRES')
print('UNO' <= 'TRES')
print('UNO' == 'TRES')
print('UNO' != 'TRES')

print(len('UNO') < len('TRES'))

#----Logicos
print('----LOG----')

print(3 > 4 and 'UNO' > 'TRES')
print(3 > 4 or 'UNO' > 'TRES')
print(3 < 4 or ('UNO' > 'TRES' and 4 == 4))
print(not(3 > 5))

#Sttrings
my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

#----Format
name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#----Destructure
language = "python"
a, b, c, d, e, f = language
print(a)

#----División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#[start, end, space]
language_slice = language[0:6:2]
print(language_slice)

reversed_language = language[::-1]
print(reversed_language)

#----Functions
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))

#Listas

myList = list()
myOtherList = []

print(len(myList))

myList = [35, 24, 62, 52, 30, 30, 17]
myOtherList = [23, '1.43', 'Na', 'Fa']

print(myList)
print(len(myList))
print(myList[0], myList[3])
print(myList[-1], myList[-3])

age, height, name, surname = myOtherList
print(name)

#----Sublistas
print(myList[2:5])

#Necesario
if True:
  print('IF TRUE')
else:
  print('IF FALSE')
  
condition = 0
while(condition < 10):
  print(condition)
  condition += 2;

while condition < 20:
    condition += 1
    if condition == 15:
        print("Se detiene la ejecución")
        break
    print(condition)

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)
    
my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
        
#functions
def sayHello():
  print('hello')

sayHello()

def sumValues(fV: int, sV: int):
  print(fV + sV)

sumValues(2,3);

def timesValues(fv, sV):
  return fv * sV
  
result = timesValues(2,3)
print(result)

def pwValues(fV: int, sV: int = 2):
  return fV ** sV
  
result: int = pwValues(3)
print(result)

def sAllValues(*values: int):
  result: int = 0
  for numb in values:
    result += numb
  return result
  
result: int = sAllValues(2,3,4,5,6,7,7)
print(result)

#Classes
class Person:
  pass
print(Person)

class Operators:
  def __init__(self, fV: int, sV: int):
    self.fV = fV
    self.sV = sV
  
  def sum(self):
    return f'sum: {self.fV + self.sV}'
  
  def divide(self):
    return f'divide: {self.fV / self.sV}'

calculator = Operators(2, 3)
print(calculator.fV)
print(calculator.sum())

calculator.fV = 3
print(calculator.divide())

#Exceptions
valueOne = 1
valueTwo = 'Hello'

try:
  print(valueOne + valueTwo)
  print('G00D')
except:
  print('ERR0R')
    
try:
    print(valueOne + valueTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")
    
try:
    print(valueOne + valueTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
    
import math
from math import pi as PI_VALUE

print(math.pi)
print(math.pow(2, 8))

print(PI_VALUE)

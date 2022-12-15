5)#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
import cmath as mth

def check(message):
 try:
  float(message)
  return True
 except ValueError:
  return False
def distance(x1,y1,x2,y2):
 if check(x1)==True and check(y1)==True and check(x2)==True and check(y2)==True:
  dist=mth.sqrt((float(x2)-float(x1))**2+((float(y2)-float(y1))**2))
  print(f'расстояние между точками = {complex(dist)}')
 else:
  print('Некорректный ввод!')
  x1 =input('введите координаты первой точки \n x: ')
  y1= input('y: ')
  x2 = input('введите координаты втрой точки \n x: ')
  y2 = input('y2: ')
  return distance(x1,y1,x2,y2)
x1 =input('введите координаты первой точки \n x: ')
y1= input('y: ')
x2 = input('введите координаты втрой точки \n x: ')
y2 = input('y2: ')
distance(x1,y1,x2,y2)

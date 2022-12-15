3)#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
def checkinput(message):
 try:
  float(message)
  return True
 except ValueError:
  return False

def coordinates(x,y):
 if checkinput(x) and checkinput(y)== True and float(x)!=0 and float(y)!=0:
  if float(x)>0 and float(y)>0:
   print('1ая четверь')
  elif float(x)>0 and float(y)<0:
   print('4ая четверть')
  elif float(x)<0 and float(y)>0:
   print('2ая четверть')
  elif float(x)<0 and float(y)<0:
   print('3тья четверь')
 else:
  print('некорректный ввод, введите x и y неравные нулю!')
  x=input('Введите x: ')
  y=input('Введите y: ')
  return coordinates(x,y)
  
x=input('Введите x: ')
y=input('Введите y: ')
coordinates(x,y)

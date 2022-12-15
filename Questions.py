4)#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def check(message):
 try:
  int(message)
  return True
 except ValueError:
  return False

def coordinatesrange(quarternumb):
 if check(quarternumb)==True and 0<int(quarternumb)<5:
  if int(quarternumb)==1:
   print('x(0, +inf], y(0, +inf)')
  elif int(quarternumb)==2:
   print('x[-inf, 0), y(0, +inf)')
  elif int(quarternumb)==3:
   print('x[-inf,0), y[-inf, 0)')
  elif int(quarternumb)==4:
   print('x[0, +inf),y(-inf, 0)')
 else:
  print('некорректный ввод! введите номер четвери от 1 до 4: ')
  
  quarternumb=input(' ')
  return coordinatesrange(quarternumb)
numbquart = input('введите номер четвери от 1 до 4: ')   
coordinatesrange(numbquart)

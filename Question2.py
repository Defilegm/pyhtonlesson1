2)#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.)
def check(x,y,z):
 left = not(x or y or z) 
 right= not x and not y and not z
 if left == right:
  return True
 else:
  return False
print(check(-1,0,0))

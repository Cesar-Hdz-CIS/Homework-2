#Cesar Hernandez 1835494
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
solution = False

for x in range(-10,11):
    for y in range(-10,11):
        if num1*x + num2*y == num3 and num4*x + num5*y == num6:
            print(x,y)
            solution = True
if not solution:
    print('No solution')
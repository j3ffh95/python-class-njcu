from math import sqrt

#Ask for A B and C and makes a quadratic formula
a = float(input("Enter Number for A: "))
b = float(input("Enter Number for B: "))
c = float(input("Enter Number for C: "))

b_equation = b**2-4*a*c

#Solving for solutions
if b_equation < 0:
    print("This equation has no real solution.")
elif  b_equation == 0:
    x = (-b+sqrt(b**2-4*a*c)) / 2*a
    print("This equation has one solution: ", x)
else:
    x1 = (-b+sqrt(b**2-4*a*c))/2*a
    x2 = (-b-sqrt(b**2-4*a*c))/2*a
    print("This equation has two solutions: ", x1, " and", x2)
from math import sqrt

#Comparin integers
m = 2
n = 4

if m * m == n :
    print("2 times 2 is 4.")

#Comparing floating-point numbers
    
x = sqrt(2)
y = 2.0

if x * x == y :
    print("sqrt(2) times sqrt(2) is 2")
else :
    print("sqrt(2) times sqrt(2) is not 2 but %.18f" % (x * x))

EPSILON = 1E -14
if abs(x * x - y) < EPSILON
    print("sqrt(2) times sqrt(2) is approximately 2")
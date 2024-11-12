#Define constants.
PENNIES_PER_DOLLAR = 100
PENNIES_PER_QUARTER = 25

#Obtain input from user.
userInput = input("Enter bill value \
(1 = $1 bill, 5 = $5 bill, etc.): ")
billValue = int(userInput)
userInput = input("Enter item price in pennies: ")
itemPrice = int(userInput)

#Compute change due.
changeDue = PENNIES_PER_DOLLAR * billValue - itemPrice
dollarCoins = changeDue // PENNIES_PER_DOLLAR
changeDue = changeDue % PENNIES_PER_DOLLAR
quarters = changeDue // PENNIES_PER_QUARTER

#Print change due.
print("Dollar coins: %3d" % dollarCoins)
print("Quarters: %6d" % quarters)


#Example of math formula and exponent

# b * (1 + r/100) ** n

b = 10
r = 100
n = 3

ans = b * (1 + r/100)**n
print("The answer of formula is: %6d" % ans)
#The root of quadratic equation

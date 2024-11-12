balance = 10.0
TARGET = 100.0
year = 0
RATE = 0.025
while balance < TARGET :
    year = year + 1
    interest = balance * RATE/100
    balance = balance + interest

print("We need ", year, " years to get our Target.")
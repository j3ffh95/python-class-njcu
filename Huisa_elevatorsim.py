'''
    This program simulates an elevator panel that skips the 13th floor
'''

#Obtain the floor number from the user as an integer
floor = int(input("Floor: "))

#Adjust floor if neseccesary
if floor == 13:
    actualFloor = floor - 1
else:
    actualFloor = floor
    
print("The elevator will travel to the actual floor", actualFloor)
METERS_PER_MILE = 1609.34
METERS_PER_FOOT = 0.3048

meters = int(input("Hello enter a meter to convert it to miles and feets: "))
 
print("It is", meters / METERS_PER_FOOT, "feet and", meters / METERS_PER_MILE, "miles")
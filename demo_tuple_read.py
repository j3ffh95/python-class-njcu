
def main() :
# Function call: assign entire value to a tuple
# date = readDate()

# Function call: use tuple assignment: 
    (month, day, year)  = readDate()
    print("month = ", month)
    print("day = ", day)
    print("year = ", year)
 
 # Function definition
def readDate() :
    print("Enter a date:")
    month = int(input(" month: "))
    day = int(input(" day: "))
    year = int(input(" year: "))
    return (month, day, year) # Returns a tuple.

main()



'''
# Ask the user for temperature and unit
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Get the state of water
state = "";
if unit.upper() == "C": # Celsius
    if temperature < 0:
        state = "Solid"

    elif 0 <= temperature < 100:
        state = "liquid"

    else:
        state = "gaseous"

elif unit.upper() == "F":  # Fahrenheit
    if temperature < 32:
        state = "solid"

    elif 32 <= temperature < 212:
        state = "liquid"

    else:
        state = "gaseous"

else:
    state = "Invalid unit"




# Print the result
if state == "Invalid unit":
    print("Error: Invalid unit provided. Please use 'C' for Celsius or 'F' for Fahrenheit.")
else:
    print(f"At {temperature}°{unit.upper()}, water is {state}.")




##################### P3.12 - Grades Conversion - Letter grade -> Number Grades, e.g. B- -> 3.0 - 0.3 = 2.7 ########################################

# Get the input from the user
letter_grade = input("Enter a letter grade (e.g., A, B+, C-, F): ").upper()

# Initialize the numeric grade
numeric_grade = 0.0

# Check the base letter grade
if letter_grade[0] == 'A':
    numeric_grade = 4.0
elif letter_grade[0] == 'B':
    numeric_grade = 3.0
elif letter_grade[0] == 'C':
    numeric_grade = 2.0
elif letter_grade[0] == 'D':
    numeric_grade = 1.0
elif letter_grade[0] == 'F':
    numeric_grade = 0.0
else:
    print("Error: Invalid letter grade")
    exit()

# Handle + or - modifiers
if len(letter_grade) > 1:
    if letter_grade[1] == '+':
        if letter_grade[0] != 'A' and letter_grade[0] != 'F':  # No A+ beyond 4.0 or F+
            numeric_grade += 0.3
    elif letter_grade[1] == '-':
        if letter_grade[0] != 'F':  # No F-
            numeric_grade -= 0.3

# Print the result
print(f"The numeric value of grade {letter_grade} is {numeric_grade:.1f}.")
'''




################################################################# P3.23 - Taxes calculations ################################################################


# Get the income input from the user
income = float(input("Enter your income: "))

# Initialize the tax variable
tax = 0.0

# Compute tax based on income brackets
if income > 500000:
    tax += (income - 500000) * 0.06
    income = 500000

if income > 250000:
    tax += (income - 250000) * 0.05
    income = 250000

if income > 100000:
    tax += (income - 100000) * 0.04
    income = 100000

if income > 75000:
    tax += (income - 75000) * 0.03
    income = 75000

if income > 50000:
    tax += (income - 50000) * 0.02
    income = 50000

if income > 0:
    tax += income * 0.01

# Print the total tax
print(f"The total tax is: ${tax:.2f}")


# Create an empty list.
values = []

# Read the input values.
print("Please enter values, Q to quit.")
userInput = input("")

# While the user input is not Q, append the value to the list.
# the append method adds the value to the end of the list.
while userInput.upper() != "Q":
    values.append(int(userInput))
    # print(values)
    userInput = input("")

# Find the largest value.
largest = values[0]
for i in range(1, len(values)):
    if values[i] > largest:
        largest = values[i]

# Print all values, marking the largest.
for element in values:
    print(element, end="")
    if element == largest:
        print(" <== largest value", end="")
    print()

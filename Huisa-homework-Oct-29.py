# Homework
# P6.2, P6.5, P6.6, P6.7

# P6.2 Write a program that reads numbers and adds them to
# a list if they aren’t already contained in the list. When the
# list contains ten numbers, the program displays the contents and quits.
'''
def main():
    numbers = []  # List to store unique numbers

    while len(numbers) < 10:
        num = input("Enter a number: ")

        if num.isdigit():  # Check if input is a positive integer
            num = int(num)
            if num not in numbers:  # Only add the number if it's not already in the list
                numbers.append(num)
                print(f"Number {num} added.")
            else:
                print(f"Number {num} is already in the list.")
        else:
            print("Please enter a valid integer.")

    # Display the contents of the list when it has 10 unique numbers
    print("\nList contains 10 unique numbers:")
    print(numbers)


# Start the program
main()
'''


'''
P6.5 Modify the largest.py program in Section 6.3 to mark both 
the smallest and the largest elements.


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
smallest = values[0]
largest = values[0]
for i in range(1, len(values)):
    if values[i] > largest:
        largest = values[i]
    elif values[i] < smallest:
        smallest = values[i]

# Print all values, marking the largest.
for element in values:
    print(element, end="")
    if element == smallest:
        print(" <== smallest value", end="")
    elif element == largest:
        print(" <== largest value", end="")
    print()
'''
'''
•• P6.6 Write a function sumWithoutSmallest that computes the sum of 
a list of values, except for the smallest one, in a single loop. 
In the loop, update the sum and the smallest value. After the loop, 
subtract the smallest value from the sum and return the difference.



def sumWithoutSmallest(values):
    sum = 0
    smallest = values[0]
    for i in range(1, len(values)):
        if values[i] < smallest:
            smallest = values[i]
        sum = sum + values[i]
    return sum - smallest


print(sumWithoutSmallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

'''
'''
• P6.7 Write a function removeMin that removes the minimum value from 
a list without using the min function or remove method.

def removeMin(numbers):
    if not numbers:  # Check if the list is empty
        return

    # Initialize min_index to the first element's index
    min_index = 0

    # Find the index of the minimum element
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i

    # Shift elements to remove the minimum element
    for i in range(min_index, len(numbers) - 1):
        numbers[i] = numbers[i + 1]

    # Remove the last element (duplicate after shifting)
    numbers.pop()


# Example usage
numbers = [45, 22, 78, 10, 99, 34, 60, 12]
print("Original list:", numbers)
removeMin(numbers)
print("List after removing minimum value:", numbers)

'''

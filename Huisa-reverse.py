# @param values a list of numbers
# @param factor the value with which to multiply each element
# @return the list values multiplied by factor
def multiply(values, factor):
    for i in range(len(values)):
        values[i] *= factor

# Prints a list in reverse order
# @param values a list of numbers
#


def printReverse(values):
    # Traverse the list in reverse order
    i = len(values) - 1
    while i >= 0:
        print(values[i], end=" ")
        i = i - 1


print(multiply([1, 2, 3], 2))
# printReverse([1, 2, 3, 4, 5])

#Read two integers and display the result of several calculation between them.

#Read the integers from the user.
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

#Compute and display the sum, difference, product, average, distance, minimum and maximun.
print("Sum of", num1, "and", num2, "=", num1 + num2 )
print(num1, "minus", num2, "=", num1 - num2 )
print(num1, "times", num2, "=", num1 * num2 )
print("The average of", num1, "and", num2, "is ", (num1 + num2) / 2 )
print("The distance of", num1, "and", num2, "is", abs(num1 - num2) )
print("The minimum of", num1, "and", num2, "is", min(num1, num2) )
print("The maximum of", num1, "and", num2, "is", max(num1, num2) )

#formater
#"%-12s%6d" %
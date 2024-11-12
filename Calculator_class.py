#Read two integers and display the result of several calculation between them.

#Read the integers from the user.
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

#Compute and display the sum, difference, product, average, distance, minimum and maximun.
print("%-12s%6d" % ("Sum:", num1 + num2 ))
print("%-12s%6d" % ("Difference:", num1 - num2 ))
print("%-12s%6d" % ("Product:", num1 * num2 ))
print("%-12s%6d" % ("Average:", (num1 + num2) / 2 ))
print("%-12s%6d" % ("Distance:", abs(num1 - num2) ))
print("%-12s%6d" % ("Minimum:", min(num1, num2) ))
print("%-12s%6d" % ("Maximum:", max(num1, num2) ))

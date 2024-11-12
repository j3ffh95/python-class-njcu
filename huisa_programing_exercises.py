import math

#• P1.1 Write a program that prints a greeting of your choice, perhaps in a language other than English.
print("Hola! Como estas?")
print()


#•• P1.2 Write a program that prints the sum of the first ten positive integers, 1 + 2 + … + 10.
max_number = 10
sum_of_numbers = max_number * (max_number + 1) // 2
print("The sum of the first ten positive integers is", sum_of_numbers)



#•• P1.3 Write a program that prints the product of the first ten positive integers, 1 × 2 × … × 10.
# (Use * to indicate multiplication in Python.)
print()
product_of_integers = math.prod(range(1, 11)) 
print("The product of the first ten positive integers is", product_of_integers)



#•• P1.4 Write a program that prints the balance of an account after the first, second, and third year.
#The account has an initial balance of $1,000 and earns 5 percent interest per year.
initial_balance = 1000
first_year = 1000 + (1000 * 0.05)
second_year = first_year + (first_year * 0.05)
third_year = second_year + (second_year * 0.05)
print()
print("Initial Balance:", "$", initial_balance, ".")
print("First Year Balance:", "$", first_year, ".")
print("Second Year Balance:", "$", second_year, ".")
print("Third Year Balance:", "$", third_year, ".")
print("")


#• P1.5 Write a program that displays your name inside a box on the screen, like this:
#Do your best to approximate lines with characters such as | - +.
print("+---------------+")
print("|   Jefferson   |")
print("+---------------+")

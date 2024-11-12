'''
    Write a program that helps a person decide whether to buy a hybrid car. Your program’s inputs should be:
•The cost of a new car
•The estimated miles driven per year
•The estimated gas price
•The efficiency in miles per gallon
•The estimated resale value after five years
Compute the total cost of owning the car for five years. (For simplicity,
we will not take the cost of financing into account.) Obtain realistic prices for a new and
used hybrid and a comparable car from the Web. Run your program twice, using today’s gas price
and 15,000 miles per year. Include pseudocode and the program runs with your assignment.
'''

# Ask user for input
car_cost = float(input("Enter the cost of a new car: $"))
miles_per_year = float(input("Enter the estimated miles driven per year: "))
gas_price = float(input("Enter the estimated gas price per gallon: $"))
efficiency = float(input("Enter the car's efficiency in miles per gallon (MPG): "))
resale_value = float(input("Enter the estimated resale value after five years: $"))

# Here we calculate the total fuel consumption over five years
total_miles = miles_per_year * 5
fuel_consumed = total_miles / efficiency

# Calculating the total fuel cost over five years
total_fuel_cost = fuel_consumed * gas_price

# This is the total cost of owning the car for five years
total_cost = (car_cost + total_fuel_cost) - resale_value


print("\nFor the given car details:")
print(f"Cost of the car: ${car_cost:,.2f}")
print(f"Estimated miles driven per year: {miles_per_year} miles")
print(f"Gas price: ${gas_price:.2f} per gallon")
print(f"Car efficiency: {efficiency} MPG")
print(f"Resale value after five years: ${resale_value:,.2f}")

print(f"\nTotal cost of owning the car for five years: ${total_cost:,.2f}")

'''
At Home HW, In our Textbook Programming exercises
P2.21 - Find the month and day for Easter Sunday of a given year.
    Easter Sunday is the first Sunday after the first full moon of spring.
    To compute the date, you can use this algorithm, invented by the mathematician Carl Friedrich Gauss in 1800:
    1.Let y be the year (such as 1800 or 2001).
    2.Divide y by 19 and call the remainder a. Ignore the quotient.
    3.Divide y by 100 to get a quotient b and a remainder c.
    4.Divide b by 4 to get a quotient d and a remainder e.
    5.Divide 8 * b + 13 by 25 to get a quotient g. Ignore the remainder.
    6.Divide 19 * a + b - d - g + 15 by 30 to get a remainder h. Ignore the quotient.
    7.Divide c by 4 to get a quotient j and a remainder k.
    8.Divide a + 11 * h by 319 to get a quotient m. Ignore the remainder.
    9.Divide 2 * e + 2 * j - k - h + m + 32 by 7 to get a remainder r. Ignore the quotient.
    10.Divide h - m + r + 90 by 25 to get a quotient n. Ignore the remainder.
    11.Divide h - m + r + n + 19 by 32 to get a remainder p. Ignore the quotient.
    Then Easter falls on day p of month n. For example, if y is 2001:
    a = 6            g = 6           m = 0    n = 4
    b = 20, c = 1    h = 18          r = 6    p = 15
    d = 5, e = 0     j = 0, k = 1
    Therefore, in 2001, Easter Sunday fell on April 15.
    Write a program that prompts the user for a year and prints out the month and day of Easter Sunday.
    
P2.16 - Draw Bull's Eye
    Write a program that reads a five-digit positive integer and breaks it into a sequence of individual digits.
    For example, the input 16384 is displayed as 1 6 3 8 4
    
    
P2.30 - Draw Olympic Rings
Write a program that displays the Olympic rings. Color the rings in the Olympic colors.

Add a few more review exercises from Ch 2 - R2.1 - R2.7
What is the value of mystery after this sequence of statements?
mystery = 1
mystery = 1 - 2 * mystery
mystery = mystery + 1


'''

mystery = 1
mystery = 1 - 2 * mystery
mystery = mystery + 1
print(mystery)
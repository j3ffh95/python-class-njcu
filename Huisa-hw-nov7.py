# Homework for Nov 7
# Programming Assignments
# 7.1, 7.2, 7.4 & 7.5

'''
• P7.1 Write a program that carries out the following tasks:
    Open a file with the name hello.txt.
    Store the message “Hello, World!” in the file.
    Close the file.
    Open the same file again.
    Read the message into a string variable and print it.

# Open the file "hello.txt" in write mode
file = open("hello.txt", "w")
# Write the message to the file
file.write("Hello, World!")
# Close the file
file.close()

# Open the file "hello.txt" in read mode
file = open("hello.txt", "r")
# Read the content into a string variable
message = file.read()
# Print the content
print(message)
# Close the file
file.close()
'''


'''
• P7.2 Write a program that reads a file containing text. Read each
line and send it to the output file, preceded by line numbers. 
If the input file is
    Mary had a little lamb 
    Whose fleece was white as snow. 
    And everywhere that Mary went, 
    The lamb was sure to go! then 
    
the program produces the output file
    /* 1 */ Mary had a little lamb 
    /* 2 */ Whose fleece was white as snow. 
    /* 3 */ And everywhere that Mary went, 
    /* 4 */ The lamb was sure to go! 
    
Prompt the user for the input and output file names.

# Prompt the user for the input and output file names
inputFileName = input("Enter the input file name: ")
outputFileName = input("Enter the output file name: ")

# Open the input file for reading and the output file for writing
inFile = open(inputFileName, "r", encoding="utf-8")
outFile = open(outputFileName, "w", encoding="utf-8")

# Initialize the line number
line_number = 1

# Read each line from the input file and write it to the output file with line numbers
for line in inFile:
    # Write the line to the output file with a line number prefix
    outFile.write(f"/* {line_number} */ {line}")
    line_number += 1

# Close both files
inFile.close()
outFile.close()

print("Lines have been written to the output file with line numbers.")
'''

'''
• P7.4 Write a program that reads a file containing two columns of 
floating-point numbers. Prompt the user for the file name. 
Print the average of each column.

# Prompt the user for input and output file names
inputFileName = input("Enter the input file name: ")
outputFileName = input("Enter the output file name: ")

# Initialize variables to store the sums and counts for each column
sum_column1 = 0.0
sum_column2 = 0.0
count = 0

try:
    # Open the input file for reading and the output file for writing
    inFile = open(inputFileName, "r", encoding="utf-8")
    outFile = open(outputFileName, "w", encoding="utf-8")
    
    # Read each line in the input file
    for line in inFile:
        # Split each line into two floating-point numbers
        values = line.split()
        if len(values) == 2:  # Ensure the line has exactly two columns
            num1 = float(values[0])
            num2 = float(values[1])
            
            # Add the numbers to the respective column sums
            sum_column1 += num1
            sum_column2 += num2
            count += 1

    # Calculate the averages and write to the output file
    if count > 0:
        average_column1 = sum_column1 / count
        average_column2 = sum_column2 / count
        outFile.write(f"Average of column 1: {average_column1:.2f}\n")
        outFile.write(f"Average of column 2: {average_column2:.2f}\n")
        print("Averages have been written to the output file.")
    else:
        outFile.write("No data to process in the file.\n")
        print("No data to process in the file.")

finally:
    # Close both files
    inFile.close()
    outFile.close()
'''

'''
•• P7.5 Write a program that asks the user for a file name and prints 
the number of characters, words, and lines in that file.
'''
filename = input("Enter the file name: ")
with open(filename, "r") as file:
    content = file.read()
    num_chars = len(content)
    num_words = len(content.split())
    num_lines = len(content.splitlines())

print(f"Number of characters: {num_chars}")
print(f"Number of words: {num_words}")
print(f"Number of lines: {num_lines}")

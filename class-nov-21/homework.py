'''
Chapter 7
toolbox
7.53 and 7.54
p7.1, p7.2, p7.5, p7.6

'''

# ================================================    Toolbox Exercises   =================================================
# ================================================   Toolbox P7.53    =================================================
'''
Toolbox P7.53 The file exercises/google.csv contains the 2014 daily stock 
data for Google, Inc.
Write a program that reads data from the CSV file and writes all data except 
the maximum and minimum columns to a new CSV file.
'''
'''
from csv import reader, writer

infile = open("google.csv", "r", encoding="utf-8")
csvReader = reader(infile)
outfile = open("google2.csv", "w", encoding="utf-8")
csvWriter = writer(outfile)

headers = ["Date", "Open", "Closing", "Shares"]
csvWriter.writerow(headers)

# Skip the row of column headers in the reader.
next(csvReader)

# FIlter the rows of data.
for row in csvReader:
    newRow = [row[0], row[1], row[2], row[3]]
    csvWriter.writerow(newRow)

infile.close()
outfile.close()
'''


# ================================================   Toolbox P7.53    =================================================


'''
• Toolbox P7.54 Write a program that reads the exam grades for multiple 
students from a text file (exercises/grades.txt) that is formatted as follows,
    Luigi
    80 69 75
    Spiny
    85 89 92
    Gumby
    78 87 82
    Arthur
    89 94 91
and creates a CSV file that can be used to create the spreadsheet shown here.
'''

'''
# Open the input file for reading
import csv
inputFile = open("exercises/grades.txt", "r")

# Open the output CSV file for writing
outputFile = open("grades.csv", "w", newline="", encoding="utf-8")
csvWriter = csv.writer(outputFile)

# Write the headers to the CSV file
csvWriter.writerow(["Name", "Exam 1", "Exam 2", "Exam 3"])

# Process each student in the input file
while True:
    # Read the student's name
    name = inputFile.readline()
    if not name:  # If no more names, break out of the loop
        break

    # Read the student's grades
    grades_line = inputFile.readline()

    # Split the grades into individual strings
    grades_strings = grades_line.split()

    # Convert each grade string to an integer using a for loop
    grades = []
    for grade in grades_strings:
        grades.append(int(grade)) 

    # Write the data to the CSV file
    csvWriter.writerow([name] + grades)

# Close the files
inputFile.close()
outputFile.close()
'''


# ================================================    Programming Exercises   =================================================
# ================================================    P7.1   =================================================
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

# ================================================    P7.2    =================================================

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
    
# Prompt the user for the input and output file names.

# Ask the user for the input and output file names
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

# ================================================    P7.5    =================================================

'''
•• P7.5 Write a program that asks the user for a file name and prints 
the number of characters, words, and lines in that file.
'''
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
'''


# ================================================    P7.6    =================================================

'''

•• P7.6 Write a program find.py that searches all files specified on the 
command line and prints out all lines containing a specified word. 
For example, if you call

    python find.py ring report.txt address.txt homework.py

then the program might print

    report.txt: has broken up an international ring of DVD bootleggers that
    address.txt: Kris Kringle, North Pole
    address.txt: Homer Simpson, Springfield
    homework.py: string = "text"

The specified word is always the first command line argument.

'''

# The first argument is the word to search for in files
import sys
search_word = sys.argv[1]
print(sys.argv[2:])
# The rest are the file names
file_names = sys.argv[2:]

# Iterate over each file
for file_name in file_names:
    try:
        # Open the file for reading
        with open(file_name, "r", encoding="utf-8") as file:
            # Iterate over each line in the file
            for line_number, line in enumerate(file, start=1):
                # Check if the search word is in the line
                if search_word in line:
                    # Print the file name, line number, and the matching line
                    print(f"{file_name}:{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error processing file '{file_name}': {e}")

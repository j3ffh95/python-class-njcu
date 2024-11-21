'''
P7.6 Write a program find.py that searches all files specified on the command
line and prints out all lines containing a specified word. For example, if you
call
    python find.py ring report.txt address.txt homework.py
then the program might print
    report.txt: has broken up an international ring of DVD bootleggers that
    address.txt: Kris Kringle, North Pole
    address.txt: Homer Simpson, Springfield
    homework.py: string = "text"
The specified word is always the first command line argument.
'''
import sys

# Check if enough arguments are provided
# if len(sys.argv) < 3:
#     print("Usage: python find.py <word> <file1> <file2> ... <etc>")
#     sys.exit(1)

# The first argument is the word to search for in files
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

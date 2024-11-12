#  Prompt the user for the number of the input and output files.
inputFileName = input("Enter the name of the input file: ")
outputFileName = input("Enter the name of the output file: ")

# Open the input and output files.
inFile = open(inputFileName, "r", encoding="utf-8")
outFile = open(outputFileName, "w", encoding="utf-8")

# Read the input and write the output.
total = 0.0
count = 0

line = inFile.readline()
while line != "":
    value = float(line)
    outFile.write("%15.2f\n" % value)
    total = total + value
    count = count + 1
    line = inFile.readline()

# Output the total and average.
outFile.write("%15s\n" % "--------------")
outFile.write("Total: %8.2f\n" % total)

average = total / count
outFile.write("Average: %6.2f\n" % average)

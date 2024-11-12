from csv import reader, writer
# Open the two csv files.
inFile = open("movies.csv", "r", encoding="utf-8")
csvReader = reader(inFile)

outFile = open("class_demo_JeffersonHuisa.csv", "w", encoding="utf-8")
csvWriter = writer(outFile)

# Add the list of column headers to the new output csv file
headers = ["Name", "Year", "Actors"]
csvWriter.writerow(headers)
next(csvReader)

# Filter the rows of data.
for row in csvReader:
    year = int(row[1])
    if year >= 1995 and year <= 2000:
        newRow = [row[0], row[1], row[4]]
        csvWriter.writerow(newRow)

inFile.close()
outFile.close()

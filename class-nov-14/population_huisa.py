##
# This program reads data  files of country populations and areas
# and prints the population density for each country.

POPULATION_FILE = "worldpop.txt"
AREA_FILE = "worldarea.txt"
REPORT_FILE = "world_pop_density.txt"


def main():
    # Open the files.
    popFile = open(POPULATION_FILE, "r", encoding="utf-8")
    areaFile = open(AREA_FILE, "r", encoding="utf-8")
    reportFile = open(REPORT_FILE, "w")

    # Read the first population data record.
    popData = extractDataRecord(popFile)
    while len(popData) == 2:
        # Read the next area data record.
        areaData = extractDataRecord(areaFile)

        # Extract the data components from the two lists.
        country = popData[0]
        population = popData[1]
        area = areaData[1]

        # Compute and print the population density.
        density = 0.0
        if area > 0:  # Protect against division by zero.
            density = population / area
        reportFile.write("%-40s%15.2f\n" % (country, density))

        # Read the next population data record.
        popData = extractDataRecord(popFile)

# Close the files.
    popFile.close()
    areaFile.close()
    reportFile.close()

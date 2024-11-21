def main():
    done = False
    while not done:
        try:
            filename = input("Please enter the file name: ")
            data = readFile(filename)

            # As an example for processing the data, we compute the sum.
            total = 0
            for value in data:
                total = total + value

            print("The sum is", total)
            done = True

        except IOError:
            print("Error: This file not found.")

        except ValueError:
            print("Error: This file contents invalid.")

        except RuntimeError as error:
            print("Error:", str(error))


def readFile(filename):
    infile = open(filename, "r", encoding="utf-8")
    data = readData(infile)
    infile.close()
    return data


def readData(infile):
    line = infile.readline()
    numberOfValues = int(line)  # May raise a ValueError exception.
    data = []

    for i in range(numberOfValues):
        line = infile.readline()
        value = float(line)  # May raise a ValueError exception.
        data.append(value)

    # Make sure there are no more values in the file.
    line = infile.readline()
    if line != "":
        raise RuntimeError("End of this file expected. There is more lines.")

    return data


main()

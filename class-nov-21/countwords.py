def main():
    uniqueWords = set()

    filename = input("Enter filename (default: nurseryrhyme.txt): ")
    if len(filename) == 0:
        filename = "nurseryrhyme.txt"
    inputFile = open(filename, "r")

    # Read the words from the file and add them to the set.
    for line in inputFile:
        theWords = line.split()
        for word in theWords:
            cleaned = clean(word)
            if cleaned != "":
                uniqueWords.add(cleaned)

    print("The document contains", len(uniqueWords), "unique words.")

    # Cleans a string by making letters lowercase and removing characters
    # that are not letters.
    # @param string the string to be cleaned
    # @return the cleaned string
    #


def clean(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char.lower()

    return result


    # Start the program.
main()

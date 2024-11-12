def main():
    # Extract the user input
    richter = float(input("Enter a magnitude on the richter scale: "))

    # Get the description and print it
    description = get_description(richter)
    print(description)

# Gets the description of an earthquake for a given magnitude
# on the Richter scale
# @param richter a float indicating the magnitude ont the richter scale
# @return a string containing the description of the damage
#


def get_description(richter):
    if richter >= 8.0:
        return "Most structures fall"
    elif richter >= 7.0:
        return "Many buildings destroyed"
    elif richter >= 6.0:
        return "Many buildings considerably damaged, some collapse"
    elif richter >= 4.5:
        return "Damage to poorly constructed buildings"
    else:
        return "No destruction of buildings"


def get_description2(richter):
    if richter >= 8.0:
        return "Most structures fall"
    if richter >= 7.0:
        return "Many buildings destroyed"
    if richter >= 6.0:
        return "Many buildings considerably damaged, some collapse"
    if richter >= 4.5:
        return "Damage to poorly constructed buildings"
    return "No destruction of buildings"


main()

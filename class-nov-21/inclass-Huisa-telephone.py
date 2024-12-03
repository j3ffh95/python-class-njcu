def main():
    myContacts = {
        "Fred": "555-1234",
        "Barney": "555-5678",
        "Wilma": "555-9012",
        "Betty": "555-3456"
    }

    printContacts(myContacts)

    # See if Fred is in the list of contacts.
    if "Fred" in myContacts:
        print("Fred's phone number is", myContacts["Fred"])
    else:
        print("Fred is not in my contact list.")

    # Get and print a list of every contact with a given number.
    nameList = findNames(myContacts, "555-3456")
    print("Names for 555-3456: ", end="")
    for name in nameList:
        print(name, end=" ")
    print()


def findNames(contacts, number):
    nameList = []
    for name in contacts:
        if contacts[name] == number:
            nameList.append(name)
    return nameList


def printContacts(contacts):
    for name in contacts:
        print(name, ":", contacts[name])


main()

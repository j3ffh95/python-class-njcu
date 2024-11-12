string = "(703)321-6753"
valid = len(string) == 13
position = 0
while valid and position < len(string):
    # print(position)
    valid = ((position == 0 and string[position] == "(")
             or (position == 4 and string[position] == ")")
             or (position == 8 and string[position] == "-")
             or (position != 0 and position != 4 and position != 8
                 and string[position].isdigit()))
    position = position + 1

# print("The number is ", valid)
if valid:
    print("The number is valid")
else:
    print("The number is invalid")

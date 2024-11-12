# In this example, the squares() function returns a list of
#  squares from 0^2 up to (n – 1)^2:
def main() :
   listSquares = squares(10)
  
   printResult(listSquares)

def squares(n) :
    result = []
    for i in range(n) :
        result.append(i * i)
    return result

def printResult(list) :

    for i in range(len(list)) :
        print(list[i], end=" ")
    print()    
# Start the program.
main()

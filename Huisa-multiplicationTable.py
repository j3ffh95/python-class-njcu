
NMAX = 10
XMAX = 10

#Print table header.
for n in range(1, NMAX) :
    print("%10d" % n, end="")
    
print()
for n in range(1, NMAX) :
    print("%10s" % "x ", end="")
    
print("\n", "   ", "-" * 90)

# Print table body.
for x in range(1, XMAX) :
    #Print the x row in the table.
    for n in range(1, NMAX) :
        print("%10.0f" % (x * n), end="")
        
    print()
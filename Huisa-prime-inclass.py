# Caution: This program has bugs.

def main():
    n = int(input("Please enter the upper limit:"))
    i = 1
    while i <= n:
        if isPrime(i):
            print(i)
        i = i + 2


# Test whether an integer is a prime number
# @param n any positive integer
# @return True if n is a prime, False otherwise

def isPrime(n):
    if n == 2:
        # 2 is the only even prime number
        return True

    if n % 2 == 0:
        # If n is even, it is not prime
        return False

    for i in range(3, n, 2):
        if n % i == 0:
            # If n is divisible by i, it is not prime
            return False
    return True


main()

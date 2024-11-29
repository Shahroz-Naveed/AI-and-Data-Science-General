# Create a function to check if a given number is prime.
num = int(input("Enter a number: "))
# Negative numbers, 0 and 1 are not primes
if num > 1:
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
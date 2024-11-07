# 7. Find the factorial of a number using a while loop.
n  = int(input("Enter a number whose factorial you want to find: "))
f = 1
if n == 0:
    print("Factorial of zero is 1")
elif n < 0 :
    print("Factorial does not exist for negative numbers") 
else:
    while n>1:
        f = f * n
        n -= 1
    print(f"Factorial of a number is {f}")   
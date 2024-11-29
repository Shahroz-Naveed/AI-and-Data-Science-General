#  3. Write a function to find the factorial of a number using recursion.
def recur_fact(n):
    if n ==1:
        return 1
    else:
        return n * recur_fact(n-1)
num = int(input("Enter factorial of a number: "))
if num < 0:
    print("Factorial of less than zero not exist.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    print("Factorial of", num, "is", recur_fact(num))
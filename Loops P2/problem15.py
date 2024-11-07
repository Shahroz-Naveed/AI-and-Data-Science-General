# 15. Print the sum of even and odd numbers separately up to a given number.
num = int(input("Enter a number whose even and odd numbers sum you want to see : "))
even_sum = 0
odd_sum = 0
for i in range(0,num+1):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print(f"Odd Sum is upto a given number is : {odd_sum}")
print(f"Sum of Even number: {even_sum}")
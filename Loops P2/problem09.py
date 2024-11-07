# 9. Write a program to print the first 10 Fibonacci numbers.
num1 = 0
num2 = 1 
for i in range(0,10,1):
    print(num1)
    next_num = num1 + num2
    num1 = num2
    num2 = next_num


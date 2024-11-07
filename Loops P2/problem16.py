# 16. Create a program to calculate the sum of the digits of an inputted integer.
num = input("Enter a number: ")
sum = 0
for i in num:
    sum =sum+ int(i)
print(f"sum of digtts is   {sum}")

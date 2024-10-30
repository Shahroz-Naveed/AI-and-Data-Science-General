# 15. Write a program to check if a number is within a specified range.
lower_range = 0
upper_range = 1000
number = int(input("Enter a number: "))
if lower_range<= number<= upper_range:
    print(f"{number} is within the range {lower_range} to {upper_range}.")
else:
    print(f"{number} is not within the range {lower_range} to {upper_range}.")
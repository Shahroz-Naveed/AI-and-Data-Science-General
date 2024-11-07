# 10. Use a loop to count the number of digits in an integer.
number = int(input("Enter a number: "))
count = 0
while number > 0 :
    count += 1
    number //=10
print(f"The number  has {count} digits.")
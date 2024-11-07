# 4. Print the multiplication table of a given number.
num = int(input("Enter the number whose table you want to see up to 10 : "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

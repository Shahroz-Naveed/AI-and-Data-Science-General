# 14. Write a program that breaks the loop when a certain condition is met.
num = int(input("Enter a  number: "))
while num > 0:
    if num >4:
        num += 1
        break
    else:
        print(num)
        num -= 1
print("Loop Break detected.")
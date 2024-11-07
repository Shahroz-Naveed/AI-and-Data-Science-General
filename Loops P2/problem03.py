# 3. Write a program to calculate the sum of all numbers between 1 and 100.
num = 1
sum = 0
# for i in range(1,num+1):
#     sum = sum + i
# print(sum)

while num <=100:
    sum = sum + num
    num += 1
print(sum)
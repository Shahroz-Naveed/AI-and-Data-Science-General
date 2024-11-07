# 20. Create a program that simulates a countdown timer starting from a given number down to zero.
import time
count_down = int(input("Enter a number for countdown rach : "))
for i in range(count_down,0,-1):
    print(i)
    time.sleep(1)
print("Times up!")
# 13. Use nested loops to print a pyramid pattern of *
row = int(input("Enter number of rows that pyramid you want to see :"))
for i in range(0,row):
    for j in range(0,row-i-1):
        print(" ", end="")
    for k in range(0,i+1):
        print("* ", end="")
    print()
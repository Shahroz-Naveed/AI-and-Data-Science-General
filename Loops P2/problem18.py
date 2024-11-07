# 18. Use a loop to print numbers in reverse order within a given range.
start_range = int(input("Enter a startign range : "))
end_range = int(input("Enter an ending range : "))
for i in range(end_range, start_range - 1, -1):
    print(i)
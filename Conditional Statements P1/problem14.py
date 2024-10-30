# 14. Check if a year input by the user is a century year. Century year is divisible by 100 and 4
year = int(input("Enter year: "))
if year % 100 == 0 and year % 4 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")
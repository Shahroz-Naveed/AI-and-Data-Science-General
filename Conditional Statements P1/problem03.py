# 3. Write a program that checks if a given year is a leap year.
year = int(input("Enter a 4 digit complete year: "))

# The condition to check if a year is a leap year is:

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.") 
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")
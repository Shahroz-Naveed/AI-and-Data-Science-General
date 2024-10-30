# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.
age = int(input("Enter you age : "))
if age < 18:
    print("You are minor ")
elif age >= 18 and age <65:
    print("you are adult ")
else:
    print("you are senior citizen ")

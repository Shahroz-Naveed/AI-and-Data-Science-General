# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
# from 0 or less than 0   -> Freezing
# between 25 to 37 -> moderate
# between 38 to 44 -> hot
celcius = int(input("Enter temperature in Celsius: "))
if celcius <= 0:
    print(f"Temperature {celcius} is freezing.")
elif celcius >=25 and celcius <=37:
    print(f"Temperature {celcius} is moderate.")
elif celcius >= 38 and celcius < 44:
    print(f"Temperature {celcius} is hot.")
else:
    print(f"Temperature {celcius} is extremely hot leave the place instantly.")
#Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:" ))
operator = input("Enter operator to perform action on numbers (+,-,*,/ )): ")
match operator:
    case '+':
        result = num1 + num2
        print(f"sum is {result}")
    case '-':
        result = num1 - num2
        print(f"difference is {result}")
    case '*':
        result = num1 * num2
        print(f"product is {result}")   
    case '/':
        result = num1 / num2
        print(f"division result is {result}")
    case _:
        print("invalid operater")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

operator=input("Enter operator(+,-,*,/,%): ")

match operator:
    case '+':print(f"Result: {num1+num2}")
    case '-':print(f"Result: {num1-num2}")
    case '*':print(f"Result: {num1*num2}")
    case '/':print(f"Result: {num1/num2}")
    case '%':print(f"Result: {num1%num2}")
    case _:print("Invalid operator")
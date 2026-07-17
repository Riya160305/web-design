def calculator():
    valid_operators = ["+","-","*","/"]

    while True:
        num1 = float(input("Enter your number: "))
        operators = input("Enter your operator(+,-,*,/): ")
        num2 = float(input("Enter your 2nd number: "))
        if operators == "+":
            result = num1 + num2
        elif operators == "-":
            result = num1 - num2
        elif operators == "*":
            result = num1 * num2
        elif operators == "/":
            if num2 == 0:
                print("Invalid as can't devide with zero")
                continue
            else:
                result = num1 / num2
        print(f"\nResult: {num1} {operators} {num2} = {result}\n")

calculator()            
        
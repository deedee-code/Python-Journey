def basic_calculator():
    print("Welcome, this is a basic calculator program.")

    first_number = int(input("Enter the first number: "))
    operator = input("Choose one of the following operator (+, -, *, /): ")
    second_number = int(input("Enter the second number: "))


    if operator == "+":
        result = first_number + second_number
        return f"{first_number} + {second_number} = {result}"
    elif operator == "-":
        result = first_number - second_number
        return f"{first_number} - {second_number} = {result}"
    elif operator == "*":
        result = first_number * second_number
        return f"{first_number} * {second_number} = {result}"
    elif operator == "/":
        if second_number == 0:
            return "Error: Division by zero is not allowed."
        else:
            result = first_number / second_number
            return f"{first_number} / {second_number} = {result}"
    else:
        return "Invalid operator"

print(basic_calculator())
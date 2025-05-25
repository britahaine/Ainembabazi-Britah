
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Error: cannot divide by zero. Please try again!")
            continue
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
        break
    except ValueError:
        print("Error: please enter a valid number.")
    
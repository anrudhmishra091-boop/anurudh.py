while True:
    operation = int(input(
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n"
        "Choose: "
    ))

    if operation < 1 or operation > 4:
        print("Error: Invalid operation")
        continue

    count = int(input("How many numbers (2, 3 or 4)? "))

    if count < 2 or count > 4:
        print("Error: Invalid number count")
        continue

    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    if count >= 3:
        num3 = float(input("Enter number 3: "))

    if count == 4:
        num4 = float(input("Enter number 4: "))

    if operation == 1:
        result = num1 + num2
        if count >= 3:
            result += num3
        if count == 4:
            result += num4
        print("Result:", result)

    elif operation == 2:
        result = num1 - num2
        if count >= 3:
            result -= num3
        if count == 4:
            result -= num4
        print("Result:", result)

    elif operation == 3:
        result = num1 * num2
        if count >= 3:
            result *= num3
        if count == 4:
            result *= num4
        print("Result:", result)

    elif operation == 4:
        result = num1 / num2
        if count >= 3:
            result /= num3
        if count == 4:
            result /= num4
        print("Result:", result)

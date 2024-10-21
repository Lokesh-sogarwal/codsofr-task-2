def calculator():
    a = float(input("Enter the 1st number: "))
    b = float(input("Enter the 2nd number: "))

    print("\nPlease select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = int(input("Choose from 1/2/3/4: "))


    if choice == 1:
        print(f"\nSum: {a} + {b} = {a + b}")
    elif choice == 2:
        print(f"\nSubtraction: {a} - {b} = {a - b}")
    elif choice == 3:
        print(f"\nMultiplication: {a} * {b} = {a * b}")
    elif choice == 4:
        if b != 0:
            print(f"\nDivision: {a} / {b} = {a / b}")
        else:
            print("\nError: Division by zero is not allowed!")
    else:
        print("\nError: Invalid operation choice.")

calculator()

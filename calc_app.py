print("\n\n\tCALCULATOR APP")
print("**Please select an option and press enter to proceed\n")
print("1. MULTIPLICATION")
print("2. ADDITION")
print("3. DIVISION")
print("4. SUBTRACTION\n")

option = int(input("Enter the preferred option: "))

if option < 1 or option > 4:
    print("Please select a valid option from 1-4")

if option == 1:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 * num2
    print(num1, "X", num2, "=", result)


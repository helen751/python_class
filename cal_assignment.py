'''Python assignment 4

1. Print “Python calculator”
2. Print the following option for the user and ask the user to choose (Addition, Multiplication, Division, Subtraction)
3. According to the option chosen by the user, ask the user to enter a number twice then perform the calculation based on the option chosen and show the user the result int his manner (first number + second number = result)
4. Also check if the user enters any option that is not specified then ask the user to enter only specified options from 1-4
5. Print thank you for using our calculation app after this


* example of what I want to see

              PYTHON CALCULATOR

**Please select an option and press enter to proceed
1. MULTIPLICATION
2. ADDITION
3. SUBTRACTION
4. DIVISION

Enter the preferred option: 2

Enter a number: 5
Enter another number: 2
5 + 2 = 7

Thank you for using our calculation App'''

#solution

print("\n\tPYTHON CALCULATOR")
print("\nPlease select an option and press enter to proceed:","\n1. MULTIPLICATION","\n2. ADDITION","\n3. SUBTRACTION","\n4. DIVISION")
option = int(input("\nEnter the preferred option: "))
num1 = int(input("\nEnter a number: "))
num2 = int(input("Enter another number: "))
if option == 1:
    result = num1 * num2
    print(num1, " X ", num2, " = ", result)
elif option == 2:
    result = num1 + num2
    print(num1, " + ", num2, " = ", result)
elif option == 3:
    result = num1 - num2
    print(num1, " - ", num2, " = ", result)
elif option == 4:
    result = num1 / num2
    print(num1, " /", num2, " = ", result)
else:
    result = "You have entered an invalid option. Please select only specified options from 1-4"


print("\nThank you for using our calculation App")
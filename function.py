numbers = [0,0,0,0,0]
for i in range(5):
    num = input("Enter Number ("+str(i) + "): ")
    numbers[i] = num
print(numbers)

name = input("What is your name: ")
def welcome():
    print("Hello", name, "Welcome to our App")

welcome()


a = 5.6N
def add(a, b, c=12):
    #local variables
    result = a + b + c
    return result
    
print(add(b=23, a=45))
int(a)



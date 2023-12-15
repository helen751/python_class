def get_user_input():
    # Accept a list of 10 numbers from the user
    numbers = []
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter a number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return numbers
numbers = get_user_input()

def display_list(numbers):
    # Display the entered list
    print("Entered list:", numbers)

display_list(numbers)

def calculate_mean(numbers):
    # Calculate the mean
    mean = sum(numbers) / len(numbers)
    print("Calculated mean: ", mean)

calculate_mean(numbers)

def calculate_median(numbers):
    # Calculate the median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]

    print("Calculated median: ", median)

calculate_median(numbers)
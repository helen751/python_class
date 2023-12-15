import random

print("\n\n\tWELCOME TO OUR GUESSING GAME")
correct_number = random.randint(1,9)
for i in range(1,6):
    num = int(input("\nPlease guess a number(1-100): "))
    
    if (num < 1 or num > 100):
        print("invalid answer! Please guess a number from 1-100")
        
    if(num == 23):
        print("Congratulations you Won!")
        break
    
    else: 
        print("You did not guess correctly. you have", (5-i), "trials remaining!")
        # Provide a hint whether the random number is even or odd
        if correct_number % 2 == 0:
            print("Hint: The correct number is even.")
        else:
            print("Hint: The correct number is odd.")

        # Provide a hint whether the random number is higher or lower than your guessed
        if correct_number > num:
            print("Hint2: The correct number is higher than your guessed number.")
        else:
            print("Hint2: The correct number is lower than your guessed number.")

else:
   print("You have exceeded your maximum trial. please restart the Game")         
    

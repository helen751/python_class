import random

print("\n\n\tWELCOME TO OUR GUESSING GAME")
correct_number = random.randint(1,100)
for i in range(1,6):
    num = int(input("\nPlease guess a number(1-100): "))
    
    if (num < 1 or num > 100):
        print("invalid answer! Please guess a number from 1-100")
        
    if(num == 23):
        print("Congratulations you Won!")
        break
    
    else: 
        print("You did not guess correctly. you have", (5-i), "trials remaining")

else:
   print("You have exceeeded your maximum trial. please restart the Game")         
    

# Guessing game

scret_num = 4

guess = int(input("Enter your guess: "))

while guess != scret_num:
    if guess < scret_num:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.") 
    guess = int(input("Enter your guess: "))       


print("Congragulations you have won the game.")        



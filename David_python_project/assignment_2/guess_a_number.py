import random

number = random.randint(1, 1000)
while True:
    guess = int(input("Guess a number between 1 - 1000: "))

    if guess > number:
        print("Too high!\nTry again")
    elif guess < number:
        print("Too low!\n Try again")
    elif guess == number:
        print("\nCongratulations\nYou guessed the number\n")
        str_continue = input("Will you try the game again: ").lower()
        if str_continue == "yes":
            continue
        elif str_continue == 'no':
            print("Thanks for playing:)")
            break

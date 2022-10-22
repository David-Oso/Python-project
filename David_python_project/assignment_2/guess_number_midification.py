import random

number = random.randint(1, 1000)
guess_number_count = 0
while True:
    guess = int(input("Guess a number between 1 - 1000: "))
    guess_number_count += 1

    if guess > number:
        print("Too high!\nTry again")
    elif guess < number:
        print("Too low!\n Try again")
    elif guess == number:
        if guess_number_count < 10:
            print("\n\nYou got lucky!")
        if guess_number_count == 10:
            print("\n\nAha! you know the secret!")
        if guess_number_count > 10:
            print("\n\nYou should be able to do better!\nWhy should it take more than 10 guesses?")
        print("\nCongratulations\nYou guessed the number\n")

        # str_continue = input("Will you try the game again: ").lower()
        # if str_continue != "yes":
        #     print("Thanks for playing:)")
        break

import random
# random.seed(104)
number = random.randint(1, 10)
counter = 0

while counter <= 3:
    guess = int(input("Guess a number between 1 ans 10: "))
    if guess == number:
        print("You guessed right")
        break
    elif guess > number:
        print("Number too high")
    elif guess < number:
        print("Number too low")
    else:
        pass
    counter += 1
else:
    print("Better luck next time, you tried guessing ordinary", number)

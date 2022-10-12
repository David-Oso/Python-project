if __name__ == "__main__":
    number = 45
    count = 0

    while count <= 3:
        guess = int(input("Enter a number between 1 and 50: "))
        if guess < number:
            print("Number too low")

        if guess > number:
            print("Number too high")
        if guess == number:
            print("Perfect.\nYou guesses right")
    count = count + 1


def reverse():
    word = input("Enter a word to check if it is a palindrome:")
    if word == word[::-1]:
        print("Perfect.\nThe word  is a palindrome")
    else:
        print("The word is not a palindrome!!")


if __name__ == '__main__':
    reverse()

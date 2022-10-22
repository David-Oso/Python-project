def is_multiple(num1, num2):
    return True if num2 % num1 == 0 else False


if __name__ == '__main__':
    number = input("Enter the two numbers: ")
    number1, number2 = number.split(',')
    print(is_multiple(int(number1), int(number2)))

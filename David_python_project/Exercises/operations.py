# number = int(input("Enter the number: "))
# operator = input("Enter the operator: ")
#
# for i in range(1, 13):
#     match operator:
#         case '+':
#             print(f'{number} + {i} = {number + i}')
#         case '-':
#             print(f"{number} - {i} = {number - i}")
#         case '*':
#             print(f'{number} * {i} = {number * i}')
#         case '/':
#             print(f"{number} / {i} = {number / i}")
#         case '^':
#             print(f'{number} ^ {i} = {number ** i}')
#         case '//':
#             print(f"{number} // {i} = {number // i}")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

match operator:
    case '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    case '-':
        print(f"{num1} - {num2} = {num1 - num2}")

    case '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    case '/':
        print(f'{num1} / {num2} = {num1 / num2}')
    case '^':
        print(f"{num1} ^ {num2} = {num1 ** num2}")
    case '//':
        print(f"{num1} // {num2} = {num1 // num2}")

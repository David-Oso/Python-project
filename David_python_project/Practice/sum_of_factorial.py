# # todo program to display sum of factors of a given number
# a = int(input("Enter a number: "))
# i = 1
# sum_0f_number = 0
# while i <= a:
#     if a % i == 0:
#         sum_0f_number = sum_0f_number + 1
#     i += 1
# print(sum_0f_number)

number = int(input("Enter a number: "))
the_sum = 0

while number != -1:
    if number % 2 == 1:
        print("Error, only even numbers please")

        number = int(input("Enter a number: "))
        continue
    the_sum += number

    number = int(input("Enter a number: "))
    print("The sum is: ", the_sum)

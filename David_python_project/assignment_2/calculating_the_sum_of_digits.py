# todo 674 % 10 = 4
#  Sum = 0 + 4 = 4
#  674 / 10 = 67
#  Second iteration
#  67 % 10 = 7
#  Sum = 4 + 7 = 11
#  67 / 10 = 6
#  Third iteration
#  6 % 10 = 6
#  Sum = 11 + 6 = 17
#  6 / 10 = 0


number = 7631

rem = 0
num = number % 10
rem += num

number // 10
num1 = (number // 10) % 10
rem += num1
print(rem)

# if __name__ == '__main__':
#     points = input("Enter the lead in points: ")
#     points_remaining = int(points)
#
#     lead_calculation = float(points_remaining - 3)
#
#     has_ball = input("Does the lead team have the ball (Yes or No): ")
#
#     if has_ball == 'Yes':
#         lead_calculation = lead_calculation + 0.5
#     else:
#         lead_calculation = lead_calculation - 0.5
#
#     if lead_calculation < 0:
#         lead_calculation = 0
#
#     lead_calculation = lead_calculation ** 2
#
#     seconds_remaining = int(input("Enter the number of seconds remaining: "))
#     if lead_calculation > seconds_remaining:
#         print("Lead is safe")
#     else:
#         print("Lead is not safe")

x = 0
while x < 10:
    print(x, end=' ')

    x = x + 1
print()
print("Final value of x: ", x)


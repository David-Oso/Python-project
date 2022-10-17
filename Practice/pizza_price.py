import math


def pizza_money(pizza_price, current_balance, offenders_amount):
    pizza_balance = pizza_price - current_balance

    expected_number_of_offenders = math.ceil(pizza_balance / offenders_amount)
    return expected_number_of_offenders


if __name__ == '__main__':
    print("The number of people remaining when the offenders amount is #100 is: ", pizza_money(10000, 4300, 100))
    print("The number of people remaining when the offenders amount is #200 is: ", pizza_money(10000, 4300, 200))
    print("The number of people remaining when the offenders amount is #500 is: ", pizza_money(10000, 4300, 500))
    print("The number of people remaining when the offenders amount is #1000 is: ", pizza_money(10000, 4300, 1000))

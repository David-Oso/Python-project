total = 0
price = 0

while True:
    product = int(input("Enter the product number(1 -- 5): "))
    quantity = int(input("Enter the quantity: "))

    match product:
        case 1:
            price = quantity * 2.98
        case 2:
            price = quantity * 4.50
        case 3:
            price = quantity * 9.98
        case 4:
            price = quantity * 4.49
        case 5:
            price = quantity * 6.87

    total += price

    more = input("Add more product? ")
    if more != "yes":
        print(f"The value of all the product sold is: ${total: .2f} ")
        break

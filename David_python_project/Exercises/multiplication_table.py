number_of_times = int(input("Enter the numbers of  table you want to print: "))

for i0 in range(1, number_of_times + 1):
    for i in range(1, 13):
        print(f"{i0} *  {i} = {i0 * i}")
    print()



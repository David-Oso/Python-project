def kelvin(temp1):
    return round(temp1 + 273.15, 2)


def celsius(temp2):
    return round(temp2 - 273.15, 2)


if __name__ == '__main__':
    temperature1 = float(input("Enter the temperature in celsius: "))
    print("Temperature in kelvin is:", kelvin(temperature1))

    temperature2 = float(input("Enter the temperature in kelvin: "))
    print("Temperature in celsius is:", celsius(temperature2))

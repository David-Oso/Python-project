import math


def hypotenuse(opp, adj):
    hyp = math.sqrt(math.pow(opp, 2) + math.pow(adj, 2))
    return hyp


if __name__ == '__main__':
    opp = float(input("Enter the opposite side of the  triangle: "))
    adj = float(input("Enter the adjacent side of the triangle: "))

    print("The hypotenuse of the triangle is:", round(hypotenuse(opp, adj), 2))

import math
radius = input("Enter the radius of your circle: ")
radius = int(radius)

circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print(f"The circumference is: {round(circumference, 2)}\
 and the area is: {round(area, 2)}")


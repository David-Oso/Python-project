# import math
# radius = input("Enter the radius of your circle: ")
# radius = int(radius)
#
# circumference = 2 * math.pi * radius
# area = math.pi * (radius ** 2)
#
# print(f"The circumference is: {round(circumference, 2)}\
#  and the area is: {round(area, 2)}")


inch = int(input("How many inches of rain has fallen: "))
volume = (inch / 12) * 435560
gallons = volume * 7.48051945
print(inch, "in. rain on 1 acre is", gallons, "gallons")
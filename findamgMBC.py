import math
AB,BC= int(input()),int(input())

AC = math.sqrt(AB**2 + BC**2)
MC = AC/2

beta = math.degrees(math.atan(BC/AB))
theta = math.degrees(math.atan(AB/BC))


print(round(theta),chr(176),sep='')

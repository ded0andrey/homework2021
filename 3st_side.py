import math
b = int(input("Enter 1st side"))
c = int(input("Enter 2st side"))
d = int(input("Enter the angle"))
a = int(math.sqrt(b**2+c**2-4*b*c*math.cos(d)))
print(a)
input()

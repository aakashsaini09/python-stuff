import math
# return sqr of a number
def sqr(n):
    return n * n
callF = sqr(4)
print("sqr is: ", callF)

# take 2 parameters and returns there sum
def sum(a, b):
    return a + b
print(sum(2,6))


# function that returns both area and circumference of a circle with given radius
def circle(redius):
    area = math.pi * redius**2
    circum = 2*math.pi*redius
    return area, circum
a, c = circle(12)
print("Area: ", round(a, 3))
print("circum: ", round(c, 3))
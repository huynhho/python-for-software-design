##def countdown(n):
##    if n == 0:
##        print("Blastoff!")
##    else:
##        print(n)
##        countdown(n-1)
import math

def area(radius):
    return math.pi* radius**2

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
##def area2(xc, yc, xp, yp):
##    radius = distance(xc, yc, xp, yp)
##    result = area(radius)
##    return result
def area2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

##def isDivisible(x, y):
##    if x % y == 0:
##        return True
##    else:
##        return False
    
def isDivisible(x, y):
    return x % y ==0

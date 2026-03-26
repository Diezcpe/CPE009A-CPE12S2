import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - (4 * a * c)
    
    if discriminant < 0:
        x1 = complex(-b, math.sqrt(abs(discriminant))) / (2 * a)
        x2 = complex(-b, -math.sqrt(abs(discriminant))) / (2 * a)
        return x1, x2
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2

print(quadratic_formula(1, 12, 32))
print(quadratic_formula(1, 2, 3))

import math

def solve_quadratic(a, b, c):
    # Calculate discriminant
    d = (b**2) - (4*a*c)
    
    # Find solutions
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        x = -b / (2*a)
        return x,
    else:
        return "No real solution"
    
def save_to_file(a, b, c, result):
    # Save to text file
    file = open("quadratic_results.txt", "a")
    file.write("=" * 40 + "\n")
    file.write(f"Equation: {a}x² + {b}x + {c} = 0\n")
    file.write(f"Answer: {result}\n")
    file.write("=" * 40 + "\n\n")
    file.close()

#Get input
print("QUADRATIC EQUATION SOLVER")
print("Equation: ax² + bx + c = 0")
print()

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))


answer = solve_quadratic(a, b, c)

# result
print()
print("=" * 40)
print(f"Equation: {a}x² + {b}x + {c} = 0")
print(f"Answer: {answer}")
print("=" * 40)

# Save
save_to_file(a, b, c, answer)
print()
print("Results saved to quadratic_results.txt")
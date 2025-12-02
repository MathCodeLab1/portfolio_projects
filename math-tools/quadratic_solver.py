import math

def solve_quadratic(a, b, c):
    if a == 0:
        return "Not a quadratic equation."

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminant) / (2*a)
        return f"Two complex roots: {real} ± {imag}i"

if __name__ == "__main__":
    print(solve_quadratic(1, -3, 2))  # Example: x² - 3x + 2 = 0
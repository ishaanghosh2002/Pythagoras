import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    side1 = float(input("Enter length of side 1: "))
    side2 = float(input("Enter length of side 2: "))
    hypotenuse = calculate_hypotenuse(side1, side2)
    print("Length of hypotenuse:", hypotenuse)

if __name__ == "__main__":
    main()
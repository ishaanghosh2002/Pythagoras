#Cython-Optimized Version

import time
from cython_pythagoras_math import calculate_hypotenuse_cython

def main():
    start_time = time.time()
    side1 = float(input("Enter length of side 1: "))
    side2 = float(input("Enter length of side 2: "))
    hypotenuse = calculate_hypotenuse_cython(side1, side2)
    print("Length of hypotenuse:", hypotenuse)
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main() 
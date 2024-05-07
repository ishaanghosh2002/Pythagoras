Pythagoras Theorem Calculator
==============================

This program calculates the length of the hypotenuse of a right triangle using the Pythagoras Theorem.

Files:
--------
- `main.py`: Unmodularized code.
- `pythagoras_math.py`: Module that contains just the `calculate_hypotenuse` function which performs the actual calculation.
- 'pythagoras.py': Module that contains the pure Python code that calls the 'calculate_hypotenuse' function from 'pythagoras_math.py'.
- 'cython_pythagoras_math.pyx': Module that contains the cythonized version of 'pythgoras_math.py'
- 'cython_pythagoras.py': Cythonized version of 'pythagoras.py' that uses 'cython_pythagoras_math.pyx'

Usage:
------
1. Run `pythagoras.py`.
2. Enter the lengths of the two sides of the right triangle when prompted.
3. The program will return the length of the hypotenuse and the execution time.
4. Run 'cython_pythagoras.py'.
5. Repeat 2
6. 3 will repeat

Example:
--------
Enter length of side 1: 3
Enter length of side 2: 4
Length of hypotenuse: 5.0

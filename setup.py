from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("cython_pythagoras_math.pyx")
)
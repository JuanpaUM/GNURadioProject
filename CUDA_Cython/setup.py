from setuptools import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    ext_modules=cythonize("scramble_kernel.pyx"),
    cmdclass={'build_ext': build_ext},
)

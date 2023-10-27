from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("scramble_kernel", ["scramble_kernel.pyx"],
                         include_dirs=["./usr/local/cuda-10.2/include"],  # Ruta completa a cuda.h
                         library_dirs=["/usr/local/cuda/lib64"])]

setup(
    name="scramble_kernel",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
)

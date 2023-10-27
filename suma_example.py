import ctypes
import numpy as np

# Cargar la biblioteca compartida
suma_kernel = ctypes.CDLL('/home/root/example/suma_kernel.so')  

# Definir los tipos de argumentos y el valor de retorno de la funcion del kernel
suma_kernel.suma_kernel.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.int32),  # a
    np.ctypeslib.ndpointer(dtype=np.int32),  # b
    np.ctypeslib.ndpointer(dtype=np.int32),  # result
    ctypes.c_int                            # size
]
suma_kernel.suma_kernel.restype = None

# Definir los arreglos de entrada
a = np.array([1, 2, 3, 4, 5], dtype=np.int32)
b = np.array([10, 20, 30, 40, 50], dtype=np.int32)
result = np.empty_like(a)

# Llamar al kernel de suma
size = len(a)
suma_kernel.suma_kernel(a, b, result, size)

# Imprimir el resultado
print("Resultado de la suma:", result)

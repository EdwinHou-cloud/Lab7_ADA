import time
import sys

def contar(arreglo):
    total = 0
    for num in arreglo:
        total += num
    return total

n = 10000000000
arreglo = list(range(n))

start_time = time.time()
resultado = contar(arreglo)
end_time = time.time()

tiempo_ejecucion = end_time - start_time
print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")

tamaño_lista = sys.getsizeof(arreglo)
tamaño_total = tamaño_lista + sys.getsizeof(resultado)
print(f"Tamño de n: {n}")
print(f"Tamaño de la lista: {tamaño_lista} bytes")
print(f"Tamaño total estimado en memoria: {tamaño_total} bytes")
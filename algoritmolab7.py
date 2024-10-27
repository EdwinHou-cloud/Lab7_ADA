import time
def algoritmolab7(arreglo, objetivo):

    for i in range(len(arreglo)):
        if arreglo[i] == objetivo:
            return i
    return -1

arreglo = [23, 15, 56, 40, 98, 100, 20, 3]
objetivo = 98

# Medición del tiempo de ejecución
inicio = time.time()  # Marca de tiempo inicial
resultado = algoritmolab7(arreglo, objetivo)  # Ejecución del algoritmo
fin = time.time()  # Marca de tiempo final

# Cálculo del tiempo de ejecución
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

if resultado != -1:
    print(f'{objetivo} se encuentra en la posicion: {resultado}')
else:
    print(f'{objetivo} no se encuentra.')

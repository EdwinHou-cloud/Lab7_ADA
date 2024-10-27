import numpy as np
import matplotlib.pyplot as plt

# Definición del rango de n
n = np.linspace(1, 100)

# Definición de las funciones de complejidad
O_n = n
O_n_log_n = n * np.log(n)
O_n_squared = n**2
O_2_n = 2**n

# Creación de la gráfica
plt.figure(figsize=(12, 8))

plt.plot(n, O_n, label='O(n)', color='blue')
plt.plot(n, O_n_log_n, label='O(n log n)', color='orange')
plt.plot(n, O_n_squared, label='O(n²)', color='green')
plt.plot(n, O_2_n, label='O(2ⁿ)', color='red')

# Configuración de la gráfica
plt.ylim(0, 200)
plt.xlim(1, 100)
plt.title('Comportamiento Asintótico de Algoritmos')
plt.xlabel('Tamaño de la Entrada (n)')
plt.ylabel('Tiempo de Ejecución')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
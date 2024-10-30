"""
Integrantes:
Hou, Edwin	        8-1021-1916
Arosemena, Miguel	8-1016-2330
Corrales, Diego		8-1001-1890
Camaño, Edward		8-1010-515
Pino, Josué		    8-1012-688
"""
import time

# Función para ingresar las ventas diarias durante una semana
def ingresar_ventas():
    ventas_semanales = []
    for i in range(7):
        dia = input(f"Ingrese las ventas del día {i + 1}: ")
        ventas_semanales.append(dia)
    return ventas_semanales

# Función para buscar y mostrar ventas en un día específico
def consultar_ventas(ventas):
    while True:
        inicio_consulta = time.time()  # Inicia el temporizador de la consulta
        
        dia = int(input("Ingrese el número de día que desea consultar (1-7): "))
        if 1 <= dia <= 7:
            print(f"Ventas del día {dia}: {ventas[dia - 1]}")
        else:
            print("Día no válido. Por favor, ingrese un número entre 1 y 7.")
        
        # Calcula y muestra el tiempo de ejecución de la consulta
        fin_consulta = time.time()
        tiempo_consulta = fin_consulta - inicio_consulta
        print(f"Tiempo de ejecución de esta consulta: {tiempo_consulta:.2f} segundos")
        
        # Pregunta si desea realizar otra consulta
        continuar = input("¿Desea consultar otro día? (s/n): ").strip().lower()
        if continuar != "s":
            print("Consulta Finalizada, vuelva pronto.")
            break

# Ejecución del algoritmo con medición de tiempo total
inicio_total = time.time()  # Inicia el temporizador total
ventas_semanales = ingresar_ventas()
consultar_ventas(ventas_semanales)
fin_total = time.time()  # Termina el temporizador total

# Calcula y muestra el tiempo total de ejecución
tiempo_total = fin_total - inicio_total
print(f"Tiempo total de ejecución del programa: {tiempo_total:.2f} segundos\n")


"""
"La empresa XYZ desea analizar su rendimiento diario y, específicamente, necesita localizar 
las ventas realizadas en un día específico. Para ello, se desarrollará un algoritmo que 
permitirá al usuario introducir las ventas realizadas por día durante una semana. Una vez 
ingresadas, el usuario podrá indicar qué día desea consultar. El algoritmo utilizará un método 
de búsqueda lineal para revisar la lista de transacciones, examinando cada entrada de manera 
secuencial hasta encontrar y mostrar todas las ventas correspondientes al día solicitado. 
Esto facilitará el análisis de datos y la toma de decisiones informadas por parte de la empresa."
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
        dia = int(input("Ingrese el número de día que desea consultar (1-7): "))
        if 1 <= dia <= 7:
            print(f"Ventas del día {dia}: {ventas[dia - 1]}")
        else:
            print("Día no válido. Por favor, ingrese un número entre 1 y 7.")
        
        # Pregunta si desea realizar otra consulta
        continuar = input("¿Desea consultar otro día? (s/n): ").strip().lower()
        if continuar != "sí":
            print("Finalizando consulta de ventas.")
            break
        
# Ejecución del algoritmo
inicio = time.time()  # Inicia el temporizador
ventas_semanales = ingresar_ventas()
consultar_ventas(ventas_semanales)
fin = time.time()  # Termina el temporizador

# Calcula y muestra el tiempo de ejecución
tiempo_total = fin - inicio
print(f"Tiempo total de ejecución: {tiempo_total:.2f} segundos")
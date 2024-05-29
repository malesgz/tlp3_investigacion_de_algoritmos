# Para comparar la eficiencia de los algoritmos mediante la medición del tiempo de ejecución de cada uno se puede utilizar la función time.time(). Esta función pertenece a una librería estándar de python que proporciona herramientas para trabajar con el tiempo en python.
import time

# Implementación de los estos algoritmos en python.
# Búsqueda lineal:
def search_linear(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

# Búsqueda binaria: 
def search_binary(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    return -1


# Prueba y comparación de tiempos de ejecución con una lista de 1 millón de elementos.
large_list = list(range(1000000))
target = 500000

# Búsqueda lineal
start_time = time.time()
linear_result = search_linear(large_list, target)
linear_search_time = time.time() - start_time

# Búsqueda binaria
start_time = time.time()
binary_result = search_binary(large_list, target)
binary_search_time = time.time() - start_time


print(f"Tiempo de ejecución de búsqueda lineal: {linear_search_time:.6f} segundos")
print(f"Tiempo de ejecución de búsqueda binaria: {binary_search_time:.6f} segundos")

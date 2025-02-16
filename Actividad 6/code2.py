from itertools import product
import matplotlib.pyplot as plt
import collections

# Generar combinaciones de 3 dados (cada uno con valores de 1 a 6)
posibles_resultados = list(product(range(1, 21), repeat=3))

# Calcular las sumas de los valores obtenidos en los 3 dados
sumas = [sum(resultado) for resultado in posibles_resultados]

# Contar frecuencias de cada suma
frecuencia = collections.Counter(sumas)

# Graficar la distribución de frecuencias
plt.bar(frecuencia.keys(), frecuencia.values(), edgecolor='black')
plt.xlabel('Suma de los dados')
plt.ylabel('Frecuencia')
plt.title('Distribución de Frecuencias de la Suma de 3 Dados')
plt.xticks(range(3, 61))
plt.show()

# Imprimir cantidad total de combinaciones
print(f"Total de combinaciones: {len(posibles_resultados)}")

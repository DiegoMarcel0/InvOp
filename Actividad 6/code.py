from itertools import product

# Generar combinaciones de 3 dados (cada uno con valores de 1 a 6)
posibles_resultados = list(product(range(1, 21), repeat=3))

# Mostrar resultados
def mostrar_resultados(resultados):
    x=0
    for resultado in resultados:
        print(resultado)
        x=x+1
    print("En total fueron ",x," posibles resultados")


# Mostrar todos los resultados posibles
mostrar_resultados(posibles_resultados)

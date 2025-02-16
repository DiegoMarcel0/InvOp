import random

def lanzar_moneda():
    return random.choice(["cara", "cruz"])

def simular_lanzamientos(n=1000):
    caras = sum(1 for _ in range(n) if lanzar_moneda() == "cara")
    return caras

# Ejecutar la simulación
n_lanzamientos = 1000
caras_obtenidas = simular_lanzamientos(n_lanzamientos)

print(f"Se lanzaron {n_lanzamientos} veces la moneda.")
print(f"Se obtuvo cara {caras_obtenidas} veces.")
print(f"Frecuencia relativa de cara: {caras_obtenidas / n_lanzamientos:.4f}")
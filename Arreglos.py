# 5 Retos con Arreglos

# 1. Buscar y devolver índice (Search)
def buscar(arreglo, valor):
    for i in range(len(arreglo)):
        if arreglo[i] == valor:
            return i
    return -1

# 2. Suma total de elementos
def suma_total(arreglo):
    suma = 0
    for i in range(len(arreglo)):
        suma += arreglo[i]
    return suma

# 3. Invertir arreglo in situ (Reverse)
def invertir(arreglo):
    inicio = 0
    fin = len(arreglo) - 1
    while inicio < fin:
        temp = arreglo[inicio]
        arreglo[inicio] = arreglo[fin]
        arreglo[fin] = temp

        inicio += 1
        fin -= 1
    return arreglo

# 4. Mover ceros al final
def mover_ceros(arreglo):
    idx_no_cero = 0

    # Mover los no ceros al inicio
    for i in range(len(arreglo)):
        if arreglo[i] != 0:
            arreglo[idx_no_cero] = arreglo[i]
            idx_no_cero += 1
    # Rellenar el resto con ceros
    for i in range(idx_no_cero, len(arreglo)):
        arreglo[i] = 0
    return arreglo

# 5. Encontrar número faltante (de 1 a n)
def numero_faltante(arreglo, n):
    suma_ideal = n * (n + 1) // 2
    suma_real = 0
    for i in range(len(arreglo)):
        suma_real += arreglo[i]
    return suma_ideal - suma_real

# Pruebas
if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50]

    print("1. Buscar 30:", buscar(numeros, 30))
    print("1. Buscar 99:", buscar(numeros, 99))
    print("2. Suma total:", suma_total(numeros))
    print("3. Invertir:", invertir([1, 2, 3, 4, 5]))
    print("4. Mover ceros:", mover_ceros([0, 1, 0, 3, 12]))
    print("5. Faltante:", numero_faltante([1, 2, 4, 5], 5))
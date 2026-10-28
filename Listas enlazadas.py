# 5 Retos con Listas Enlazadas

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None
    # 1. InsertAtEnd (insertar al final)
    def insert_at_end(self, dato):
        nuevo_nodo = Nodo(dato)

        # Si Cabeza es null, el nuevo nodo es la Cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        # Si no, recorrer hasta que actual.siguiente sea null
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    # 2. Invertir lista (pregunta de entrevista)
    def invertir(self):
        prev = None
        actual = self.cabeza
        sig = None
        while actual is not None:
            sig = actual.siguiente      # guardar el siguiente
            actual.siguiente = prev     # invertir la flecha
            prev = actual               # avanzar prev
            actual = sig                # avanzar actual
        self.cabeza = prev

    # 3. Devolver el nodo N desde el final
    def nodo_desde_final(self, n):
        rapido = self.cabeza
        lento = self.cabeza
        # Avanzar el Rápido N pasos primero
        for _ in range(n):
            if rapido is None:          # N es mayor que el tamaño de la lista
                return None
            rapido = rapido.siguiente
        # Mover ambos 1 paso a la vez hasta que Rápido sea null
        while rapido is not None:
            rapido = rapido.siguiente
            lento = lento.siguiente
        return lento

    # 4. Eliminar duplicados (lista ordenada)
    def eliminar_duplicados(self):
        actual = self.cabeza
        while actual is not None and actual.siguiente is not None:
            if actual.dato == actual.siguiente.dato:
                # Saltar el nodo repetido
                actual.siguiente = actual.siguiente.siguiente
            else:
                # Avanzar solo si no hubo duplicado
                actual = actual.siguiente

    # 5. Detectar bucle (liebre y tortuga)
    def tiene_bucle(self):
        lento = self.cabeza
        rapido = self.cabeza
        while rapido is not None and rapido.siguiente is not None:
            lento = lento.siguiente                # avanza 1 paso
            rapido = rapido.siguiente.siguiente    # avanza 2 pasos
            if lento == rapido:
                return True
        return False

    # Auxiliar: mostrar la lista
    def mostrar(self):
        actual = self.cabeza
        resultado = ""
        while actual is not None:
            resultado += str(actual.dato) + " -> "
            actual = actual.siguiente
        print(resultado + "null")

# Pruebas
if __name__ == "__main__":
    # 1. InsertAtEnd
    print("1. InsertAtEnd")
    lista = Lista()
    lista.insert_at_end(10)
    lista.insert_at_end(20)
    lista.insert_at_end(30)
    lista.mostrar()

    # 2. Invertir
    print("\n2. Invertir")
    lista.invertir()
    lista.mostrar()

    # 3. Nodo N desde el final
    print("\n3. Nodo N desde el final")
    lista3 = Lista()
    for numero in [10, 20, 30, 40, 50]:
        lista3.insert_at_end(numero)
    print(lista3.nodo_desde_final(1).dato)   # 50
    print(lista3.nodo_desde_final(2).dato)   # 40
    print(lista3.nodo_desde_final(5).dato)   # 10
    print(lista3.nodo_desde_final(9))        # None

    # 4. Eliminar duplicados
    print("\n4. Eliminar duplicados")
    lista4 = Lista()
    for numero in [1, 1, 2, 3, 3, 3]:
        lista4.insert_at_end(numero)
    lista4.mostrar()
    lista4.eliminar_duplicados()
    lista4.mostrar()

    # 5. Detectar bucle
    print("\n5. Detectar bucle")
    lista5 = Lista()
    for numero in [10, 20, 30, 40]:
        lista5.insert_at_end(numero)
    print(lista5.tiene_bucle())              # False

    # Crear un bucle a propósito: el último nodo apunta al segundo
    ultimo = lista5.cabeza
    while ultimo.siguiente is not None:
        ultimo = ultimo.siguiente
    ultimo.siguiente = lista5.cabeza.siguiente
    print(lista5.tiene_bucle())              # True
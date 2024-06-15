#Mario Alberto Gomez Temores 21310159   14/06/24

def selection_sort(arr):
    """
    Funcion para ordenar una lista usando el algoritmo de seleccion.

    :param arr: Lista de elementos a ordenar.
    """
    # Obtenemos el tamano de la lista.
    n = len(arr)
    
    # Iteramos sobre cada elemento de la lista.
    for i in range(n):
        # Suponemos que el primer elemento no ordenado es el menor.
        min_idx = i
        
        # Iteramos sobre los elementos restantes para encontrar el menor.
        for j in range(i + 1, n):
            # Si encontramos un elemento menor, actualizamos min_idx.
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Si encontramos un nuevo elemento menor, lo intercambiamos con el elemento actual.
        # Esta operacion pone al menor elemento en su posicion correcta.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # Mostramos el estado actual de la lista despues de cada intercambio.
        print(f"Iteracion {i+1}: {arr}")

# Lista de ejemplo para ordenar.
example_list = [64, 25, 12, 22, 11]

# Llamamos a la funcion de ordenamiento.
selection_sort(example_list)

# Mostramos la lista ordenada final.
print("Lista ordenada:", example_list)


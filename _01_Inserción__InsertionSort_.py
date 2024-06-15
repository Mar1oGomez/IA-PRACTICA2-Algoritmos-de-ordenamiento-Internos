def insertion_sort(arr):
    # Define la funcion de ordenamiento por insercion que recibe una lista 'arr' como argumento.

    # Itera sobre el arreglo desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        # 'i' es el indice del segundo elemento hasta el ultimo elemento del arreglo.

        # Guarda el valor actual en una variable temporal
        key = arr[i]
        # 'key' es el valor del elemento en la posicion 'i' que se va a insertar en el subarreglo ordenado.

        # Inicializa j como el indice anterior al actual
        j = i - 1
        # 'j' es el indice del elemento anterior al actual.

        # Mueve los elementos del arreglo que son mayores que el valor actual
        # a una posicion adelante de su posicion actual
        while j >= 0 and key < arr[j]:
            # Mientras 'j' no sea negativo y el valor en 'arr[j]' sea mayor que 'key':
            arr[j + 1] = arr[j]
            # Mueve el valor de 'arr[j]' una posicion adelante.
            j -= 1
            # Decrementa 'j' para seguir comparando con los elementos anteriores.

        # Coloca el valor actual en su posicion correcta dentro del subarreglo ordenado
        arr[j + 1] = key
        # Inserta 'key' en la posicion correcta en el subarreglo ordenado.

# Ejemplo de uso:
arr = [12, 11, 13, 5, 6]
# Define un arreglo de ejemplo para ser ordenado.

print("Arreglo original:", arr)
# Imprime el arreglo original.

insertion_sort(arr)
# Llama a la funcion de ordenamiento por insercion para ordenar el arreglo.

print("Arreglo ordenado:", arr)
# Imprime el arreglo ordenado.

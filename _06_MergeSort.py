#Mario Alberto Gomez Temores 21310159   14/06/24
def merge_sort(arr):
    # Define la funcion merge_sort que toma un arreglo 'arr' como parametro
    if len(arr) <= 1:
        # Si la longitud del arreglo es 1 o menos, el arreglo ya esta ordenado
        return arr

    mid = len(arr) // 2
    # Encuentra el punto medio del arreglo

    left_half = arr[:mid]
    # Divide el arreglo en la mitad izquierda

    right_half = arr[mid:]
    # Divide el arreglo en la mitad derecha

    left_sorted = merge_sort(left_half)
    # Llama recursivamente a merge_sort en la mitad izquierda

    right_sorted = merge_sort(right_half)
    # Llama recursivamente a merge_sort en la mitad derecha

    return merge(left_sorted, right_sorted)
    # Combina las dos mitades ordenadas usando la funcion 'merge' y retorna el resultado

def merge(left, right):
    # Define la funcion merge que toma dos arreglos ordenados 'left' y 'right'
    result = []
    # Inicializa un arreglo vacio para el resultado

    left_index = 0
    # Inicializa el indice para recorrer la mitad izquierda

    right_index = 0
    # Inicializa el indice para recorrer la mitad derecha

    while left_index < len(left) and right_index < len(right):
        # Mientras haya elementos en ambas mitades
        if left[left_index] <= right[right_index]:
            # Si el elemento actual de la izquierda es menor o igual al de la derecha
            result.append(left[left_index])
            # Anade el elemento de la izquierda al resultado
            left_index += 1
            # Avanza al siguiente elemento de la izquierda
        else:
            result.append(right[right_index])
            # Si el elemento de la derecha es menor, anadelo al resultado
            right_index += 1
            # Avanza al siguiente elemento de la derecha

    result.extend(left[left_index:])
    # Agrega cualquier elemento restante de la izquierda

    result.extend(right[right_index:])
    # Agrega cualquier elemento restante de la derecha

    return result
    # Retorna el arreglo combinado y ordenado

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
# Define un arreglo de ejemplo

print("Arreglo original:", arr)
# Imprime el arreglo original

sorted_arr = merge_sort(arr)
# Llama a merge_sort en el arreglo y guarda el resultado

print("Arreglo ordenado:", sorted_arr)
# Imprime el arreglo ordenado


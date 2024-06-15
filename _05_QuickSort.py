#Mario Alberto Gomez Temores 21310159   14/06/24
def quicksort(arr):
    # Funcion principal que toma un array y lo ordena usando QuickSort

    if len(arr) <= 1:
        # Si el array tiene 0 o 1 elementos, ya esta ordenado
        return arr

    # Elegimos el pivote como el ultimo elemento del array
    pivot = arr[-1]
    
    # Creamos dos listas, una para los elementos menores al pivote y otra para los mayores
    left = []
    right = []
    
    # Iteramos sobre todos los elementos menos el pivote
    for x in arr[:-1]:
        if x <= pivot:
            # Si el elemento es menor o igual al pivote, lo anadimos a la lista izquierda
            left.append(x)
        else:
            # Si el elemento es mayor al pivote, lo anadimos a la lista derecha
            right.append(x)
    
    # Llamamos recursivamente a quicksort en las sublistas izquierda y derecha
    # y combinamos los resultados con el pivote en el medio
    return quicksort(left) + [pivot] + quicksort(right)

# Ejemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
print("Array original:", arr)
sorted_arr = quicksort(arr)
print("Array ordenado:", sorted_arr)


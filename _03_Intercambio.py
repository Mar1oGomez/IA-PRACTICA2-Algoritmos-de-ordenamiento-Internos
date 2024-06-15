#Mario Alberto Gomez Temores 21310159   14/06/24

# Definimos una funcion llamada bubble_sort que recibe una lista de elementos
def bubble_sort(arr):
    # Obtenemos la longitud de la lista
    n = len(arr)
    
    # Iteramos a traves de todos los elementos de la lista
    for i in range(n):
        # Dentro del primer bucle, iteramos desde el principio de la lista hasta el penultimo elemento no ordenado
        for j in range(0, n-i-1):
            # Comparamos el elemento actual con el siguiente
            if arr[j] > arr[j+1]:
                # Si el elemento actual es mayor que el siguiente, los intercambiamos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Aqui utilizamos la tecnica de desempaquetado para intercambiar los valores
        
        # Imprimimos el estado de la lista despues de cada iteracion del primer bucle para ver el progreso
        print(f'Iteracion {i+1}: {arr}')
        
    # Devolvemos la lista ordenada (esto es opcional ya que la lista se ordena en su lugar)
    return arr

# Lista de ejemplo a ordenar
lista = [64, 34, 25, 12, 22, 11, 90]

# Llamamos a la funcion bubble_sort pasando la lista de ejemplo
print("Lista original:", lista)
sorted_lista = bubble_sort(lista)

# Imprimimos la lista ordenada
print("Lista ordenada:", sorted_lista)


#Mario Alberto Gomez Temores 21310159   14/06/24
def counting_sort(arr, exp):
    # Creamos un array de tamano 10 para almacenar el conteo de ocurrencias
    count = [0] * 10
    # Este array almacenara el resultado ordenado temporalmente
    output = [0] * len(arr)

    # Contamos el numero de ocurrencias de cada digito en la posicion exp
    for i in range(len(arr)):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Modificamos count[i] para que contenga la posicion de este digito en output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construimos el array output usando count para ubicar los elementos
    for i in range(len(arr) - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copiamos el array output al array original arr, para que arr contenga los numeros ordenados segun el digito actual
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontramos el numero maximo para saber el numero de digitos
    max1 = max(arr)

    # Aplicamos counting_sort para cada digito. Empezamos con el digito menos significativo.
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Array original:")
print(arr)

radix_sort(arr)

print("Array ordenado:")
print(arr)


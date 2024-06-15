#Mario Alberto Gomez Temores 21310159   14/06/24

class TreeNode:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None  # Hijo izquierdo del nodo
        self.right = None  # Hijo derecho del nodo

def insert(root, value):
    if root is None:
        return TreeNode(value)  # Si el arbol esta vacio, crea un nuevo nodo con el valor dado
    else:
        if value < root.value:
            root.left = insert(root.left, value)  # Inserta en el subarbol izquierdo si el valor es menor que el valor del nodo
        else:
            root.right = insert(root.right, value)  # Inserta en el subarbol derecho si el valor es mayor o igual que el valor del nodo
    return root

def inorder_traversal(root, result):
    if root is not None:
        inorder_traversal(root.left, result)  # Recorre el subarbol izquierdo en orden
        result.append(root.value)  # Agrega el valor del nodo actual a la lista de resultados
        inorder_traversal(root.right, result)  # Recorre el subarbol derecho en orden

def tree_sort(arr):
    if not arr:
        return []  # Si el array esta vacio, devuelve una lista vacia

    root = TreeNode(arr[0])  # Crea el nodo raiz con el primer elemento del array
    for value in arr[1:]:
        insert(root, value)  # Inserta el resto de los elementos en el arbol

    sorted_arr = []
    inorder_traversal(root, sorted_arr)  # Realiza un recorrido en orden del arbol y llena sorted_arr con los elementos ordenados
    return sorted_arr

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [5, 3, 7, 2, 4, 8, 1]
    print("Array original:", arr)
    sorted_arr = tree_sort(arr)
    print("Array ordenado:", sorted_arr)

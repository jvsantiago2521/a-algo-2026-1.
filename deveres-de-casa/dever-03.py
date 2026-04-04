def verifica_palindromo(array, inicio, fim):
    if inicio >= fim:
        return True
    
    if array[inicio] != array[fim]:
        return False
    
    return verifica_palindromo(array, inicio + 1, fim - 1)

array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

arrays = [array1, array2, array3, array4]

for i, arr in enumerate(arrays, 1):
    resultado = verifica_palindromo(arr, 0, len(arr) - 1)
    
    print(f"array{i}: {arr}")
    if resultado:
        print("É palíndromo")
    else:
        print("Não é palíndromo")
    print()
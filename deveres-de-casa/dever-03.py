def verifica_palindromo(array, inicio, fim):
    """
    verifica se um array eh palindromo usando recursao

    logica:
    compara o primeiro elemento com o ultimo
    se forem diferentes, nao eh palindromo
    se forem iguais, continua comparando para dentro

    para quando inicio >= fim (caso base)
    """
    if inicio >= fim:
        return True
    
    if array[inicio] != array[fim]:
        return False
    
    return verifica_palindromo(array, inicio + 1, fim - 1)


"""
arrays de teste para verificar diferentes casos
"""
array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]


"""
lista que junta todos os arrays para facilitar o teste
"""
arrays = [array1, array2, array3, array4]


"""
para cada array:
- chama a funcao
- verifica se eh palindromo
- mostra o resultado
"""
for i, arr in enumerate(arrays, 1):
    resultado = verifica_palindromo(arr, 0, len(arr) - 1)
    
    print(f"array{i}: {arr}")
    if resultado:
        print("É palíndromo")
    else:
        print("Não é palíndromo")
    print()

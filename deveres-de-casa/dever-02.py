import time

# funcao recursiva para calcular fatorial
def fatorial(n):
"""
calcula o fatorial de um numero n

logica:
se n for 0 ou 1, retorna 1 (caso base)
senao, chama a funcao novamente com n-1
"""
    # caso base: quando n eh 0 ou 1, o resultado eh 1
    if n == 0 or n == 1:
        return 1
    
    # caso recursivo:
    # chama a funcao novamente diminuindo n
    return n * fatorial(n - 1)


# lista de valores que vamos testar
valores = [10, 100, 500, 1000]

"""
para cada valor de n:
- mede o tempo antes
- calcula o fatorial
- mede o tempo depois
- mostra o resultado
"""
for n in valores:
    
    inicio = time.time()
    
    resultado = fatorial(n)
    
    fim = time.time()
    
    tempo = fim - inicio

    print(f"n = {n}")
    print(f"Tempo: {tempo:.6f} segundos")
    print("-" * 30)

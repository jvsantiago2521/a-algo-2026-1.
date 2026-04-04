import time

# Função recursiva para calcular fatorial
def fatorial(n):
    # Caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    return n * fatorial(n - 1)


# Valores de n para teste
valores = [10, 100, 500, 1000]

for n in valores:
    inicio = time.time()
    
    resultado = fatorial(n)
    
    fim = time.time()
    tempo = fim - inicio

    print(f"n = {n}")
    print(f"Tempo: {tempo:.6f} segundos")
    print("-" * 30)
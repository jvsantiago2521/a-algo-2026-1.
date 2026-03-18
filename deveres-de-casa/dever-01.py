
"""
calculo de fatorial utilizando recursao e medicao de tempo de execucao

autor: João Victor Santiago
"""

import time

def calcular_fatorial(n: int) -> int:
    """
    calcula o fatorial de um numero inteiro n utilizando recursao

    :param n: numero inteiro nao negativo
    :return: fatorial de n
    """
    # caso base: fatorial de 0 e 1
    if n == 0:
        return 1

    # caso recursivo: n * fatorial(n-1)
    return n * calcular_fatorial(n - 1)


def medir_tempo_execucao(n: int) -> float:
    """
    mede o tempo de execucao da funcao de fatorial com maior precisao
    """
    inicio = time.perf_counter()

    calcular_fatorial(n)

    fim = time.perf_counter()

    return fim - inicio


def main():
    """
    funcao principal do programa
    """
    # entrada do usuario
    numero = int(input("Digite um numero inteiro: "))

    resultado = calcular_fatorial(numero)

    print(f"Fatorial de {numero} = {resultado}")

    # testes de desempenho
    valores_teste = [10, 100, 500, 1000]

    print("\ntempo de execucao:")
    for valor in valores_teste:
        try:
            tempo = medir_tempo_execucao(valor)
            print(f"n = {valor} -> tempo = {tempo:.6f} segundos")
        except RecursionError:
            print(f"n = {valor} -> erro: limite de recursao atingido")


if __name__ == "__main__":
    main()

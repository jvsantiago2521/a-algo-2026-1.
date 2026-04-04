import math

def f(n):
    """
    calcula F(n) usando recursao

    logica:
    caso base: F(1) = 2
    caso recursivo: F(n) = 2 * F(n-1) + n^2
    """
    if n == 1:
        return 2
    return 2 * f(n - 1) + n**2


def f_fechada(n):
    """
    calcula F(n) usando a formula fechada

    logica:
    usa a expressao matematica direta
    sem precisar de chamadas recursivas
    """
    return int(6 * (2 ** (n - 1)) - n**2 - 4*n - 6)

n = int(input("Digite o valor de n: "))

"""
verifica se o valor eh valido
se for, calcula pelos dois metodos e mostra o resultado
"""
if n < 1:
    print("Digite um valor de n maior ou igual a 1")
else:
    resultado_recursivo = f(n)

    resultado_fechado = f_fechada(n)

    print(f"F({n}) recursao: {resultado_recursivo}")
    print(f"F({n}) formula fechada: {resultado_fechado}")

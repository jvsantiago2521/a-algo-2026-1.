import math

def f(n):
    if n == 1:
        return 2
    return 2 * f(n - 1) + n**2

def f_fechada(n):
    return int(6 * (2 ** (n - 1)) - n**2 - 4*n - 6)

n = int(input("Digite o valor de n: "))

if n < 1:
    print("Digite um valor de n maior ou igual a 1")
else:
    resultado_recursivo = f(n)

    resultado_fechado = f_fechada(n)

    print(f"F({n}) recursao: {resultado_recursivo}")
    print(f"F({n}) formula fechada: {resultado_fechado}")
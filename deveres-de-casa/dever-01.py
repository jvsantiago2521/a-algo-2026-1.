import random
import time

def insertion_sort(lista):
"""
funcao que ordena uma lista usando insertion sort

funcionamento:
percorre a lista e vai colocando cada elemento
na posicao correta comparando com os anteriores
"""
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

# lista de tamanhos que vamos testar
tamanhos = [1000, 5000, 10000, 20000, 50000]

"""
parte principal

aqui vamos:
- gerar listas aleatorias
- ordenar com insertion sort
- ordenar com sorted()
- comparar o tempo dos dois
"""
for n in tamanhos:
    lista = [random.randint(0, 100000) for _ in range(n)]

    lista_insertion = lista.copy()
    inicio = time.time()
    insertion_sort(lista_insertion)
    fim = time.time()
    tempo_insertion = fim - inicio

    lista_sorted = lista.copy()
    inicio = time.time()
    sorted(lista_sorted)
    fim = time.time()
    tempo_sorted = fim - inicio

    print()
    print(f"Insertion Sort: {tempo_insertion:.6f} segundos")
    print(f"sorted(): {tempo_sorted:.6f} segundos")
    print()

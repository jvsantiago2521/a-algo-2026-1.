# Dever 01 - Cálculo de Fatorial Recursivo

## Descrição

Este projeto implementa um algoritmo em Python para calcular o fatorial de um número inteiro utilizando **recursão**.  

Também foi realizada a medição do tempo de execução para diferentes valores de entrada, com o objetivo de analisar como o tempo cresce em função do tamanho da entrada.

---

## Execução

O programa solicita um número inteiro ao usuário e calcula seu fatorial.

Além disso, realiza testes automáticos para os seguintes valores:

- 10
- 100
- 500
- 1000

---

## Saída obtida no terminal

```bash
Digite um número inteiro: 10
Fatorial de 10 = 3628800

Tempo de execução:
n = 10 -> tempo = 0.000004 segundos
n = 100 -> tempo = 0.000047 segundos
n = 500 -> tempo = 0.000351 segundos
n = 1000 -> erro: limite de recursão atingido
```
Obs: Os tempos podem variar dependendo da máquina.

---

## Observação

Para valores grandes como n = 1000, ocorre erro de recursão devido ao limite padrão do Python (RecursionError).

---

## Análise de Complexidade

O algoritmo de fatorial recursivo segue a seguinte relação de recorrência:

T(n) = T(n-1) + 1

Isso ocorre porque, para calcular o fatorial de n, o algoritmo chama a si mesmo com n-1, até atingir o caso base (n = 0).

Expandindo essa relação:

T(n) = T(n-1) + 1  
T(n) = T(n-2) + 2  
...  
T(n) = T(0) + n  

Logo:

T(n) = n

---

## Conclusão

A complexidade de tempo do algoritmo é:

O(n)

Ou seja, o tempo de execução cresce de forma linear em relação ao tamanho da entrada

Quando o valor de n aumenta, o número de operações também aumenta proporcionalmente.

## Considerações finais

Mesmo sendo eficiente para valores pequenos, essa recursiva tem limitaçoes devido ao limite de recursão da linguagem, sendo melhor para fins didáticos do que para grandes valores de entrada

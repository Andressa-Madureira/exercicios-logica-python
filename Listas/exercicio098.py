#%%
"""
Exercicio 098
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
----------------------------------------------------
Este programa tem como objetivo gerar um vetor com 5 números inteiros e, a partir dele,
realizar três ações:

1. Exibir a multiplicação de todos os elementos do vetor.
2. Exibir a soma de todos os elementos do vetor.
3. Exibir os próprios números do vetor.

Para facilitar essas operações, foi utilizada a biblioteca NumPy, que oferece recursos
eficientes para manipulação de arrays e cálculos matemáticos.

O vetor foi criado com a função np.arange(1, 6), que gera uma sequência de números inteiros
de 1 até 5. O número final (6) é exclusivo, ou seja, não é incluído na sequência.

As funções utilizadas foram:
- np.prod(): calcula o produto de todos os elementos do vetor.
- np.sum(): calcula a soma de todos os elementos do vetor.
- print(): exibe os resultados no terminal.
"""

import numpy as np

numeros = np.arange(1,6)

print(np.prod(numeros))
print(np.sum(numeros))
print(numeros)
# %%

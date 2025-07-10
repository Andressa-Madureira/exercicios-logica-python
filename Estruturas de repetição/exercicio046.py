#%%
"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

OBS: converter a virgula do decimal 
"""

nota_solicitada = float(input("Por favor, digite um número entre 0 e 10: "))

while nota_solicitada > 10 or nota_solicitada < 0:
    nota_solicitada = float(input("Nota inválida!Por favor, digite uma nota entre 0 e 10: "))

print(f"A nota {nota_solicitada} é válida")   
# %%

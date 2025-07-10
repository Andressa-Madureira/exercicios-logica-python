#%%
"""
Faça um Programa que peça um valor e mostre na tela se o valor é
positivo ou negativo.
"""

verificar_valor = int(input("Por favor, digite um número: "))

if verificar_valor == 0:
    print(f"O {verificar_valor} é um número neutro.")
    verificar_valor = int(input("Por favor, tente novamente: "))

if verificar_valor < 0:
    print(f"O número {verificar_valor} é negativo")
    

if verificar_valor > 0:
    print(f"O número {verificar_valor} é positivo")
  



# %%

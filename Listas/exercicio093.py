#%%
"""
Exercicio 093 
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
vetor_real = []

for i in range(10):
    numero_real = (input(f"Digite o número desejado: "))

    numero_real = float(numero_real)

    vetor_real.append(numero_real)

for numero in vetor_real[::-1]:
    print(f"{numero}")

    


# %%

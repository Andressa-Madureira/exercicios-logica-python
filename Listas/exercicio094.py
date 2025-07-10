#%%
"""
Exercicio 094
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []

contador = 1

while contador < 5:
    nota_digitada = input(f"Por favor, digite a {contador}° nota: ")
    nota_digitada = nota_digitada.replace(",",".")
    nota_digitada = float(nota_digitada)
    
    contador = contador + 1
    notas.append(nota_digitada)
    
soma = sum(notas)
resultado = soma / 4  
print(f"Nota: {notas} - Média: {resultado}")
print(notas)
    

    


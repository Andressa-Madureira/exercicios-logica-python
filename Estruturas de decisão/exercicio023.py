#%%
"""
Exercicio 023
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

primeira_nota = input("Qual é a primeira nota? ")
segunda_nota = input("Qual é a segunda nota? ")

primeira_nota = primeira_nota.replace(",",".")
segunda_nota = segunda_nota.replace(",",".")

primeira_nota = float(primeira_nota)
segunda_nota = float(segunda_nota)

resultado_media = (primeira_nota + segunda_nota) / 2

if resultado_media == 10:
    print("Aprovado com distinção")
elif resultado_media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

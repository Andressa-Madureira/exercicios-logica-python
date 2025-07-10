#%%

"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
primeira_nota = float(input(
    "Qual é a nota do primeiro bimestre? "
))

segunda_nota = float(input(
    "Qual é a nota do segundo bimestre?"
))

terceira_nota = float(input(
    "Qual é a nota do terceiro bimestre?"
))

quarta_nota = float(input(
    "Qual é a nota do quarto bimestre? "
))

resultado_media = (primeira_nota + segunda_nota+ terceira_nota + quarta_nota) / 4

print("O resultado da média é: ", resultado_media)
# %%

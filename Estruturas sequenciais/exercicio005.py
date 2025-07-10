#%%
"""
Exercicio 005
Faça um Programa que converta metros para centímetros.
"""



converter_numero = input("Por favor, informe quantos metros você precisa que eu converta? ")

converter_numero = converter_numero.replace("," , ".")

converter_numero = float(converter_numero)

numero_convertido = (converter_numero * 100)



print(f"{converter_numero} metros é igual a {numero_convertido} centímetros")


# %%

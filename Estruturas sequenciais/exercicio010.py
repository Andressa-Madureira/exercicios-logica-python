#%%
"""
Exercicio 010
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
"""

temperatura_celsius = input("Quantos graus celsius?")

temperatura_celsius = temperatura_celsius.replace(",", ".")

temperatura_celsius = float(temperatura_celsius)

temperatura_Farenheit = (temperatura_celsius * 9 / 5) + 32 


print(f"{temperatura_celsius}°C é igual a {temperatura_Farenheit}°F")
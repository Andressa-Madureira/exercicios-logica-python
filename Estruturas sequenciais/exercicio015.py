#%%
"""
Exercicio 015
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.


Documentado:
Este trecho do programa coleta as informações básicas para o cálculo do salário mensal.

- Solicita ao usuário o valor que ele ganha por hora (ganho_hora).
- Solicita ao usuário o total de horas trabalhadas no mês (horas_trabalhadas).
- Converte as entradas para inteiros para possibilitar cálculos futuros.
- Exibe os valores coletados para conferência.

Observação:
A multiplicação do ganho por hora pelo número de horas trabalhadas será usada para calcular o salário bruto posteriormente.

"""

#Preciso pegar o GANHO por hora e multiplicar pelas HORAS trabalhadas no mês. Esse valor é o resultado do salário bruto

ganho_hora = int(input("Quanto você ganha por hora? "))

horas_trabalhadas = int(input("Quantas horas trabalhadas?"))

print(ganho_hora)
print(horas_trabalhadas)

# %%

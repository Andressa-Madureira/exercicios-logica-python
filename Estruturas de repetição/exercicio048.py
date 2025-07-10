#%%
"""
Exercicio 048
Faça um programa que leia e valide as seguintes informações: Nome: maior que 3 caracteres; Idade: entre 0 e 150; Salário: maior que zero; Sexo: 'f' ou 'm'; Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Digite o seu nome:")
while len(nome) < 3:
 nome = input("Seu nome precisa ter 3 caracteres ou mais. Escreva seu nome completo: ")
print(nome)
idade = int(input("Digite a sua idade: "))
while idade < 0 or idade > 150:
 idade = int(input("Você precisa digitar sua idade corretamente. Sua idade precisa ser entre 0 e 150 anos"))
print(idade)
salario = float(input("Qual é o seu salário?"))
while salario <= 0 :
 salario = float(input("Seu salário não pode ser menor que 0. Por favor, insira o valor do seu salário corretamente:"))
print(salario)

sexo_feminino =  "F"
sexo_masculino = "M"

sexo_digitado = input("Por favor, digite o sexo. F para feminino e M para masculino: ").upper()

while sexo_digitado != sexo_feminino and sexo_digitado!= sexo_masculino:
    sexo_digitado = input("Sexo inválido! Por favor, digite F para feminino e M para masculino").upper()
print(sexo_digitado)



solteiro = 'S'
casado = 'C'
viuvo = 'V'
divorciado = 'D'

estado_civil_solicitado = input("Qual é o seu estado civil? Digite 's' para Solteiro, 'c' para Casado, 'v' para Viúvo e 'd' para Divorciado").upper()

while estado_civil_solicitado != solteiro and estado_civil_solicitado != casado and estado_civil_solicitado != viuvo and estado_civil_solicitado != divorciado:
    estado_civil_solicitado = input("Estado civil inválido. Digite 's' para Solteiro, 'c' para Casado, 'v' para Viúvo e 'd' para Divorciado").upper()

print(estado_civil_solicitado)
# %%

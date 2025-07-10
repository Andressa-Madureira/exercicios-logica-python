#%%
"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

login_usuario = input("Qual é o seu nome? ")


senha_usuario = input("Por favor, digite a sua senha: ")



while senha_usuario.lower() == login_usuario.lower():
    senha_usuario = input("Senha inválida! A senha não pode ser o seu nome. Por favor, digite uma senha válida: ")

print(f"Usuário cadastrado com sucesso!\nNome usuário: {login_usuario}\n Senha usuário: {senha_usuario}")



# %%

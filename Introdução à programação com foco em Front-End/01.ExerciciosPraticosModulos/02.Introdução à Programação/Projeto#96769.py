""""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2022.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2023).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
"""

rodarWhile = True

while rodarWhile:
    nomeUsuario = input("Informe seu nome: ")
    try:
        anoNascimentoUsuario = int(input("Informe o ano de seu nascimento: "))
        
        if  anoNascimentoUsuario >= 1962 or anoNascimentoUsuario <= 2022:
            idadeUsuario = 2023 - anoNascimentoUsuario
            print(f"Olá {nomeUsuario}! \nSua idade no ano de 2023 é de {idadeUsuario} ano(s)")
            rodarWhile = False
        else:
            print("Você nasceu em um ano fora do intervalo permitido.")
        
    except ValueError:
        print("O ano informado está com a formatação incorreta.")

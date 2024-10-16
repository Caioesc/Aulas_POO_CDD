from biblioteca import *
"""try:
    a = 4
    b = 0
    divisao = a/b
    print(divisao)
except ZeroDivisionError:
    print("Não é possível dividir por zero.")"""

"""try:
    print(x)
except NameError:
    print("A variável escolhida não existe")"""

"""try:
    num = int(input("digite um número")
    print(num)
except SyntaxError:
    print("Algo está digitado de forma errada.")"""

"""try:
    num = int(input("Digite um número:"))
    divisão = "num"/num
except TypeError:
    print("Tipo de dado usado na divisão errada!")"""

"""try:
    frutas = ["banana", "laranja", "pera"]
    print(frutas[3])
except IndexError:
    print("Índice do vetor não existe")"""

# //--------------------//--------ARQUIVOS----------//--------------------//---------------------//

opcao = 0
while opcao != 3:
    opcao = int(input("Digite a opção desejada:\n1 - Gravar \n2 - Mostrar \n3 - Sair"))

    if opcao == 1:
        nome = input("Digite um nome: ")
        gravar(nome)
    elif opcao == 2:
        print("Nomes do arquivo:\n")
        mostrar()
    elif opcao == 3:
        print("Programa encerrado!")
        opcao = 3
    else:
        print("Opção inválida.")
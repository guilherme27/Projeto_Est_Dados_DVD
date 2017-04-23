from functions import *
import os, sys, time

Locadora = BST()
LDE = "Locadora de Estrutura\n"

print(LDE)
login = input("Login: ")
os.system("cls")
print(LDE)
senha = input("Senha: ")
os.system("cls")

while True:
    cond1 = True
    while cond1 == True:
        os.system("cls")
        print(LDE)
        print("Escolha uma opção:\n1 - Buscar filme\n2 - Listar todos os filmes\n3 - Adicionar filme\n4 - Remover filme\n5 - Sair\n")
        try:
            option = int(input())
            cond1 = False
        except ValueError:
            os.system("cls")
            print(LDE, "\nPor favor, escolha algo válido.")
            time.sleep(3)
    if option == 1:
        os.system("cls")
        print(LDE)
        cond2 = True
        while cond2 == True:
            try:
                os.system("cls")
                print(LDE)
                type = int(input("1 - Por código\n2 - Por nome\n3 - Por categoria\n4 - Voltar\n\n"))
                cond2 = False
                if type == 1:
                    os.system("cls")
                    print(LDE)
                    data = int(input("Código: "))
                    if Locadora.search(type, data) == None:
                        os.system("cls")
                        print(LDE, "\nFilme não encontrado.")
                        time.sleep(3)
                        cond2 = True
                    else:
                        a, b, c, d, e = Locadora.search(type, data)
                        os.system("cls")
                        print(LDE)
                        print("Código do DVD:", a, "\nNome do filme:", b, "\nGênero:", c, "\nSituação:", d, "\nValor do aluguel:", e, "\n")
                        input("Pressione enter para continuar")
                        cond1 = True
                elif type == 2:
                    os.system("cls")
                    print(LDE)
                    data = input("Nome: ")
                    data = data.lower()
                    if Locadora.search(type, data) == None:
                        os.system("cls")
                        print(LDE, "\nFilme não encontrado.")
                        time.sleep(3)
                        cond2 = True
                    else:
                        a, b, c, d, e = Locadora.search(type, data)
                        os.system("cls")
                        print(LDE)
                        print("Código do DVD:", a, "\nNome do filme:", b, "\nGênero:", c, "\nSituação:", d, "\nValor do aluguel:", e)
                        input("Pressione enter para continuar")
                        cond1 = True

                elif type == 3:
                    os.system("cls")
                    print(LDE)
                    print("Opção ainda não implementada. Tente novamente em futuras atualizações.")
                    time.sleep(3)
                elif type == 4:
                    cond1 = True
                    break
                else:
                    os.system("cls")
                    print(LDE, "\nPor favor, escolha algo válido.")
                    time.sleep(3)
                    cond2 = True
            except ValueError:
                os.system("cls")
                print(LDE, "\nPor favor, escolha algo válido.")
                time.sleep(3)
                cond2 = True

    if option == 2:
        print("Opção ainda não implementada. Tente novamente em futuras atualizações.")

    if option == 3:
        os.system("cls")
        print(LDE)
        code = int(input("Código: "))
        os.system("cls")
        print(LDE)
        name = input("Filme: ")
        name = name.lower()
        os.system("cls")
        print(LDE)
        gender = input("Gênero: ")
        gender = gender.lower()
        os.system("cls")
        print(LDE)
        value = int(input("Valor: "))
        os.system("cls")
        Locadora.insert(code, name, gender, "disponível", value)
        cond1 = True
        os.system("cls")
        print(LDE)
        print("Filme adicionado.")
        time.sleep(2)
    if option == 5:
        break

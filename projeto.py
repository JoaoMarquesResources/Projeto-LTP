import random

ListaEquipas = []

while True:
    print("\n----- MENU -----")
    print("1 - Gerir Equipas")
    print("2 - Gerir Jogos e Classificações")
    print("3 - Sair")
    print("----------------")

    opcao = int(input("Opção: "))

    if opcao >= 1 and opcao <= 3:
        if opcao == 1:
            while True:
                equipas = int(input("\nNúmero de Equipas: "))

                if equipas < 3:
                    print("ERRO: Numero de equipas inválido")
                else: break
            
            for i in range(0, equipas):
                nome = str(input("\nNome da Equipa: "))

                while True:
                    numJogadores = int(input("Número de jogadores da equipa: "))

                    if numJogadores < 5:
                        print("ERRO: Número de Jogadores inválido!")
                    else:
                        ListaEquipas.append(nome)
                        ListaEquipas.append(numJogadores)
                        break
            print(ListaEquipas)

        elif opcao == 2:
            for i in range(0, equipas):
                #gerar random os resultados

        else: break
    else:
        print("\nERRO: Opção não existe!")
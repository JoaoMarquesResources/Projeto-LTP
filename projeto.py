import random

#--------Variáveis principais--------
ListaEquipas = []
NumJogadoresEquipa = []
JogadoresDaEquipa = []
PosicaoJogadores = []
#--------Variáveis auxiliares--------
vez = 0

while True:
    print("\n----- MENU -----")
    print("1 - Gerir Equipas")
    print("2 - Gerir Jogos e Classificações")
    print("3 - Sair")
    print("----------------")

    opcao = int(input("Opção: "))

    if opcao >= 1 and opcao <= 3:
        if opcao == 1:
            vez += 1

            if vez == 1:
                while True:
                    equipas = int(input("\nNúmero de Equipas: "))

                    if equipas < 3:
                        print("ERRO: Numero de equipas inválido")
                    else: break
                
                for i in range(0, equipas):
                    nomeEquipa = str(input("\nNome da Equipa: "))

                    while True:
                        numJogadores = int(input("Número de jogadores da equipa: "))

                        if numJogadores < 5 or numJogadores > 12:
                            print("ERRO: Número de Jogadores inválido!")
                        else:
                            ListaEquipas.append(nomeEquipa)
                            NumJogadoresEquipa.append(numJogadores)
                            break
                    
                    print(f"----- Jogadores da equipa {nomeEquipa} -----")
                    for i in range(0, numJogadores):
                        print(f"  Jogador {i + 1}  ")
                        nome = str(input("Nome do jogador: "))
                        JogadoresDaEquipa.append(nome)
                        while True:
                            posicao = str(input(f"O jogador {nome} é Titular ou Suplente (t/s): "))
                            if posicao == "t" or posicao == "s":
                                PosicaoJogadores.append(posicao)
                                break
                            else: print("ERRO: Posição inválida!")
                    print(38*"-")

                print(ListaEquipas)
                print(NumJogadoresEquipa)
                print(JogadoresDaEquipa)
                print(PosicaoJogadores)
            else:
                print("\n----- MENU DE GESTÃO DE EQUIPAS -------")
                print("1 - Retirar jogador à equipa")
                print("2 - Adicionar jogador à equipa")
                print("3 - Trocar posição do jogador")
                print("---------------------------------------")

                opcao2 = int(input("Opção: "))

                if opcao2 == 1:
                    print(f"Equipas: {ListaEquipas}")

                    i = 0
                    check = False
                    while True:
                        EscolhaEquipa = input("Para qual equipa deseja retirar um jogador: ")

                        for j in range(0, len(ListaEquipas)):
                            if EscolhaEquipa == ListaEquipas[j]:
                                check = True
                                aux = j
                        
                        if check: break
                        else: print("ERRO: Equipa não exite!")
                        i += 1
                    
                    print("Jogadores:")
                    
                    aux2 = NumJogadoresEquipa[aux]

                    for i in range(0, NumJogadoresEquipa[aux]):
                        print((aux2 - 1) + i)
                        print(f"Jogador {i + 1}: {JogadoresDaEquipa[(aux2 - 1) + i]}")
                    
                    jogador = int(input("Nº do jogador a retirar: "))

                    NumJogadoresEquipa[aux] -= 1
                    JogadoresDaEquipa.pop((aux2 - 1) + jogador - 1)
                    PosicaoJogadores.pop((aux2 - 1) + jogador - 1)

                    print(NumJogadoresEquipa)
                    print(JogadoresDaEquipa)
                    print(PosicaoJogadores)

        elif opcao == 2:
            print("opçao 2")
            #for i in range(0, equipas):
                #gerar random os resultados

        else: break
    else:
        print("\nERRO: Opção não existe!")
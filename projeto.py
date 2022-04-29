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
                print("\n------ MENU DE GESTÃO DE EQUIPAS ------")
                print("1 - Retirar jogador à equipa")
                print("2 - Adicionar jogador à equipa")
                print("3 - Trocar posição do jogador")
                print("---------------------------------------")

                opcao2 = int(input("Opção: "))

                if opcao2 == 1:
                    print(f"Equipas: {ListaEquipas}")     
                    while True:
                        equipa = input("Nome da equipa para remover jogador: ")
                        if equipa in ListaEquipas:
                            pos = ListaEquipas.index(equipa)
                            if NumJogadoresEquipa[pos] > 5:
                                aux = pos
                                break
                            else:
                                print("ERRO: Tamanho da equipa ficará menor que 5!")
                        else:
                            print("ERRO: Nome da equipa inválido!")

                    while True:
                        jogador = input(f"\nNome do jogador a remover da equipa {equipa}: ")

                        aux = -1
                        aux2 = 0
                        
                        for i in range(0, len(NumJogadoresEquipa)):
                            if i == 0: cena = 0
                            else: cena += NumJogadoresEquipa[i - 1]

                            for j in range(cena, cena + NumJogadoresEquipa[i]):
                                if JogadoresDaEquipa[j] == jogador:
                                    aux = i
                                    aux2 = JogadoresDaEquipa.index(jogador)
                        
                        if aux == pos:
                            break
                        else:
                            print(f"ERRO: O jogador: {jogador} não faz parte da equipa: {equipa}")

                    NumJogadoresEquipa[aux] -= 1
                    JogadoresDaEquipa.pop(aux2)
                    PosicaoJogadores.pop(aux2)

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
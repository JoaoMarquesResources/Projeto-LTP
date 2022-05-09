import random

#--------Variáveis principais--------
ListaEquipas = []
NumJogadoresEquipa = []
JogadoresDaEquipa = []
PosicaoJogadores = []
#--------Variáveis auxiliares--------
vez = 0
gerir = False

ler = open('jogadores.txt', 'r')
conteudo = ler.read()

if conteudo == "": gerir = True
ler.close()

def atualizarFicheiro():
    fich = open('jogadores.txt', 'w')

    #Escrever no ficheiro a informação
    for i in range(0, len(ListaEquipas)):
        fich.write(f"{ListaEquipas[i]} ")
    fich.write("\n")

    for i in range(0, len(NumJogadoresEquipa)):
        fich.write(f"{NumJogadoresEquipa[i]} ")
    fich.write("\n")

    for i in range(0, len(JogadoresDaEquipa)):
        fich.write(f"{JogadoresDaEquipa[i]} ")
    fich.write("\n")

    for i in range(0, len(PosicaoJogadores)):
        fich.write(f"{PosicaoJogadores[i]} ")
    fich.write("\n")

    fich.close()

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
            if vez == 1 and gerir:

                while True:
                    equipas = int(input("\nNúmero de Equipas: "))

                    if equipas < 3 or equipas > 10:
                        print("ERRO: Numero de equipas inválido")
                    else: break
                
                for i in range(0, equipas):
                    nomeEquipa = input("\nNome da Equipa: ")

                    while True:
                        numJogadores = int(input("Número de jogadores da equipa: "))

                        if numJogadores < 5 or numJogadores > 11:
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
                            posicao = input(f"O jogador {nome} é Titular ou Suplente (t/s): ")
                            if posicao == "t" or posicao == "s":
                                PosicaoJogadores.append(posicao)
                                break
                            else: print("ERRO: Posição inválida!")
                    print(38*"-")

                print(ListaEquipas)
                print(NumJogadoresEquipa)
                print(JogadoresDaEquipa)
                print(PosicaoJogadores)

                atualizarFicheiro()

                #gerir = False

            else:
                print("\n------ MENU DE GESTÃO DE EQUIPAS ------")
                print("1 - Retirar jogador à equipa")
                print("2 - Adicionar jogador à equipa")
                print("3 - Trocar posição do jogador")
                print("---------------------------------------")

                #Buscar o conteudo ao ficheiro
                if gerir == False:
                    ler = open('jogadores.txt', 'r')
                    
                    n = 0
                    palavras = ler.readlines()
                    
                    for line in palavras:
                        n = n + 1
                        for word in line.split():
                            if n == 1: ListaEquipas.append(str(word))
                            if n == 2: NumJogadoresEquipa.append(int(word))
                            if n == 3: JogadoresDaEquipa.append(str(word))
                            if n == 4: PosicaoJogadores.append(str(word))
                    
                    gerir = True
                    ler.close()

                opcao2 = int(input("Opção: "))

                if opcao2 == 1:
                    print(f"Equipas: {ListaEquipas}")     
                    while True:
                        equipa = input("Nome da equipa para remover jogador: ")
                        if equipa in ListaEquipas:
                            pos = ListaEquipas.index(equipa)
                            if NumJogadoresEquipa[pos] > 5:
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

                    atualizarFicheiro()

                elif opcao2 == 2:
                    print(f"Equipas: {ListaEquipas}")     
                    while True:
                        equipa = input("Nome da equipa para adicionar jogador: ")
                        if equipa in ListaEquipas:
                            pos = ListaEquipas.index(equipa)
                            if NumJogadoresEquipa[pos] < 11:
                                break
                            else:
                                print("ERRO: Tamanho da equipa ficará maior que 11!")
                        else:
                            print("ERRO: Nome da equipa inválido!")

                    while True:
                        jogador = input(f"\nNome do jogador a adicionar na equipa {equipa}: ")
                        
                        while True:
                            ts = input("Titular ou suplente (t/s): ")

                            if ts == "t" or ts == "s": break
                            else: print("ERRO: Posição inválida!")

                        for i in range(0, len(NumJogadoresEquipa)):
                            if i == 0: cena = 0
                            else: cena += NumJogadoresEquipa[i - 1]

                            if i == pos:
                                JogadoresDaEquipa.insert(cena + NumJogadoresEquipa[i], jogador)
                                PosicaoJogadores.insert(cena + NumJogadoresEquipa[i], ts)

                        NumJogadoresEquipa[pos] += 1

                        print(NumJogadoresEquipa)
                        print(JogadoresDaEquipa)
                        print(PosicaoJogadores)

                        atualizarFicheiro()
                        break
                elif opcao2 == 3:
                    while True:
                        jog = input("Nome do jogador: ")

                        for i in range(0, len(JogadoresDaEquipa)):
                            if JogadoresDaEquipa[i] == jog:
                                break
                        
                        print("ERRO: Jogador não exite!")


        elif opcao == 2:
            print("opçao 2")
            #for i in range(0, equipas):
                #gerar random os resultados

        else: break
    else:
        print("\nERRO: Opção não existe!")
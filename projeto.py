import math

#--------Variáveis principais--------
ListaEquipas = []
NumJogadoresEquipa = []
JogadoresDaEquipa = []
PosicaoJogadores = []
pontos = []
jogos = []
classificacoes = []
golosSofridos = []
#--------Variáveis auxiliares--------
vez = 0
gerir = False

ler = open('Projeto-LTP/jogadores.txt', 'r')
conteudo = ler.read()

#Verificar se o ficheiro tem conteudo
if conteudo == "": gerir = True
ler.close()

def atualizarFicheiro():
    fich = open('Projeto-LTP/jogadores.txt', 'w')

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

def buscarConteudo(g):
    if g == False:
        ler = open('Projeto-LTP/jogadores.txt', 'r')
        
        n = 0
        palavras = ler.readlines()
        
        if len(ListaEquipas) == 0:
            for line in palavras:
                n = n + 1
                for word in line.split():
                    if n == 1: ListaEquipas.append(str(word))
                    if n == 2: NumJogadoresEquipa.append(int(word))
                    if n == 3: JogadoresDaEquipa.append(str(word))
                    if n == 4: PosicaoJogadores.append(str(word))
        
        g = True
        ler.close()

def gerirEquipas():
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
            nome = str(input(f"Nome do jogador {i + 1}: "))
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

def retirarJogador():
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

def adicionarJogador():
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

def mudarPos():
    while True:
        jog = input("Nome do jogador: ")

        if jog in JogadoresDaEquipa:
            i = JogadoresDaEquipa.index(jog)
            break
        else: print("ERRO: Jogador não exite!")

    pos = input("Posição nova do jogador (t/s): ")

    PosicaoJogadores[i] = pos

    print(NumJogadoresEquipa)
    print(JogadoresDaEquipa)
    print(PosicaoJogadores)

def GerirClassificacoes():
    for i in range(0, len(ListaEquipas)):
        pontos.append(0)
        golos.append(0)
        golosSofridos.append(0)

    for i in range(0, len(ListaEquipas) - 1):
        for j in range(i, len(ListaEquipas) - 1):
            print(f"-------- {ListaEquipas[i]} x {ListaEquipas[j + 1]} --------")
            x = int(input(f"Golos {ListaEquipas[i]}: "))
            y = int(input(f"Golos {ListaEquipas[j + 1]}: "))
            classificacoes.append(x)
            classificacoes.append(y)
            jogos.append(ListaEquipas[i])
            jogos.append(ListaEquipas[j + 1])

    for i in range(0, len(classificacoes), 2):
        if classificacoes[i] > classificacoes[i + 1]:
            pontos[ListaEquipas.index(jogos[i])] += 3
        elif classificacoes[i] < classificacoes[i + 1]:
            pontos[ListaEquipas.index(jogos[i + 1])] += 3
        else:
            pontos[ListaEquipas.index(jogos[i])] += 1
            pontos[ListaEquipas.index(jogos[i + 1])] += 1
    
    for i in range(0, len(ListaEquipas)):
        for j in range(0, len(classificacoes)):
            if ListaEquipas[i] == jogos[j]:
                golos[i] += classificacoes[j]

    for i in range(0, len(classificacoes), 2):
        aux = ListaEquipas.index(jogos[i])
        golosSofridos[aux] += classificacoes[i + 1]
        aux = ListaEquipas.index(jogos[i + 1])
        golosSofridos[aux] += classificacoes[i]
    
while True:
    print("\n----- MENU -----")
    print("1 - Gerir Equipas")
    print("2 - Gerir Jogos e Classificações")
    print("3 - Sair")
    print("----------------")

    opcao = int(input("Opção: "))

    if opcao == 1:
        vez += 1
        if vez == 1 and gerir:
            gerirEquipas()
            gerir = False
            atualizarFicheiro()
        else:
            while True:
                print("\n------ MENU DE GESTÃO DE EQUIPAS ------")
                print("1 - Retirar jogador à equipa")
                print("2 - Adicionar jogador à equipa")
                print("3 - Trocar posição do jogador")
                print("4 - Voltar")
                print("---------------------------------------")

                g = gerir
                buscarConteudo(g)

                opcao2 = int(input("Opção: "))

                if opcao2 == 1:
                    retirarJogador()
                    atualizarFicheiro()
                    break
                elif opcao2 == 2:
                    adicionarJogador()
                    atualizarFicheiro()
                    break
                elif opcao2 == 3:
                    mudarPos()
                    atualizarFicheiro()
                    break
                elif opcao2 == 4:
                    break
                else:
                    print("ERRO: Opção inválida!")

    elif opcao == 2:
        if gerir == False:
            pontos = []
            golos = []
            jogos = []
            classificacoes = []
            golosSofridos = []

            buscarConteudo(gerir)
            GerirClassificacoes()

            #---------------- PRINTAR CLASSIFICAÇÕES -------------------
            print(jogos)
            print(classificacoes)
            print(pontos)
            print(golos)
            print(golosSofridos)

            m = max(pontos)
            m2 = min(golosSofridos)
            aux = pontos.count(m)
            pos = pontos.index(m)
            aux2 = golosSofridos.index(m2)

            auxiliar = []
            for i in range(0, len(pontos)):
                if pontos[i] == m:
                    auxiliar.append(golosSofridos[i])
                else: auxiliar.append(math.inf)

            if aux != 1: print(f"Vencedor {ListaEquipas[auxiliar.index(min(auxiliar))]}")

            else: print(f"Vencedor: {ListaEquipas[pos]}")

        else: print("ERRO: Ainda não criou as equipas!")

    elif opcao == 3: break

    else: print("\nERRO: Opção não existe!")
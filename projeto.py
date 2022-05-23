import time
from colorama import init
from termcolor import colored
import math
from tabulate import tabulate

#--------Variáveis principais--------
ListaEquipas = []
NumJogadoresEquipa = []
JogadoresDaEquipa = []
PosicaoJogadores = []
pontos = []
jogos = []
classificacoes = []
golosSofridos = []
jogosJogados = []
historico = {"hist":[], "data":[]}
#--------Variáveis auxiliares--------
vez = 0
gerir = False

ler = open('Projeto-LTP/jogadores.txt', 'r')
conteudo = ler.read()

#Verificar se o ficheiro tem conteudo
if conteudo == "": gerir = True
ler.close()

init()

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

    for i in range(0, len(historico["hist"])):
        h = historico["hist"][i]
        fich.write(f"{h}.")
    fich.write("\n")

    for i in range(0, len(historico["hist"])):
        d = historico["data"][i]
        fich.write(f"{d}.")

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
                    elif n == 2: NumJogadoresEquipa.append(int(word))
                    elif n == 3: JogadoresDaEquipa.append(str(word))
                    elif n == 4: PosicaoJogadores.append(str(word))
                
                for word in line.split("."):
                    if word != "\n" and word != "":
                        if n == 5: historico["hist"].append(str(word))
                        elif n == 6: historico["data"].append(str(word))
        
        g = True
        ler.close()

def gerirEquipas():
    while True:
        equipas = int(input(colored("\nNº de equipas: ", "green")))

        if equipas < 3 or equipas > 10:
            print(colored("ERRO: Numero de equipas inválido", "red"))
        else: break
    
    for i in range(0, equipas):
        nomeEquipa = input(colored(f"\nNome da Equipa {i + 1}: ", "yellow"))

        while True:
            numJogadores = int(input(colored("Número de jogadores da equipa: ", "green")))

            if numJogadores < 5 or numJogadores > 11:
                print(colored("ERRO: Número de Jogadores inválido!", "green"))
            else:
                ListaEquipas.append(nomeEquipa)
                NumJogadoresEquipa.append(numJogadores)
                break
        
        print(f"\n----- Jogadores da equipa {nomeEquipa} -----")
        for i in range(0, numJogadores):
            nome = str(input(colored(f"Nome do jogador {i + 1}: ", "green")))
            JogadoresDaEquipa.append(nome)
            while True:
                posicao = input(colored(f"O jogador {nome} é Titular ou Suplente (t/s): ", "green"))
                if posicao == "t" or posicao == "s":
                    PosicaoJogadores.append(posicao)
                    break
                else: print(colored("ERRO: Posição inválida!", "red"))
        print(38*"-")

    historico["hist"].append("Equipas Criadas")
    historico["data"].append(time.asctime())

    printarListas()

def retirarJogador():
    print(f"Equipas: {ListaEquipas}")     
    while True:
        equipa = input(colored("Nome da equipa para remover jogador: ", "green"))
        if equipa in ListaEquipas:
            pos = ListaEquipas.index(equipa)
            if NumJogadoresEquipa[pos] > 5:
                break
            else:
                print(colored("ERRO: Tamanho da equipa ficará menor que 5!", "red"))
        else:
            print(colored("ERRO: Nome da equipa inválido!", "red"))

    while True:
        jogador = input(colored(f"\nNome do jogador a remover da equipa {equipa}: ", "green"))

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
            print(colored(f"ERRO: O jogador: {jogador} não faz parte da equipa: {equipa}", "red"))

    NumJogadoresEquipa[aux] -= 1
    JogadoresDaEquipa.pop(aux2)
    PosicaoJogadores.pop(aux2)

    print(colored("\n--- Alterações ---", "blue"))
    f = f"Removeu o jogador {jogador} da equipa {equipa}"
    print(f)
    time1 = time.asctime()
    
    historico["hist"].append(f)
    historico["data"].append(time1)

def adicionarJogador():
    print(f"Equipas: {ListaEquipas}")     
    while True:
        equipa = input(colored("Nome da equipa para adicionar jogador: ", "green"))
        if equipa in ListaEquipas:
            pos = ListaEquipas.index(equipa)
            if NumJogadoresEquipa[pos] < 11:
                break
            else:
                print(colored("ERRO: Tamanho da equipa ficará maior que 11!", "red"))
        else:
            print(colored("ERRO: Nome da equipa inválido!", "red"))

    jogador = input(colored(f"\nNome do jogador a adicionar na equipa {equipa}: ", "green"))

    while True:
        ts = input(colored("Titular ou suplente (t/s): ", "green"))

        if ts == "t" or ts == "s": break
        else: print(colored("ERRO: Posição inválida!", "red"))

    for i in range(0, len(NumJogadoresEquipa)):
        if i == 0: cena = 0
        else: cena += NumJogadoresEquipa[i - 1]

        if i == pos:
            JogadoresDaEquipa.insert(cena + NumJogadoresEquipa[i], jogador)
            PosicaoJogadores.insert(cena + NumJogadoresEquipa[i], ts)

    NumJogadoresEquipa[pos] += 1

    print(colored("\n--- Alterações ---", "blue"))
    f = f"Adicionou o jogador {jogador}({ts}) na equipa {equipa}"
    print(f)
    time1 = time.asctime()
    
    historico["hist"].append(f)
    historico["data"].append(time1)

def mudarPos():
    while True:
        jog = input(colored("Nome do jogador: ", "green"))

        if jog in JogadoresDaEquipa:
            i = JogadoresDaEquipa.index(jog)
            break
        else: print(colored("ERRO: Jogador não exite!", "red"))

    while True:
        pos = input(colored("Posição nova do jogador (t/s): ", "green"))

        if pos == "t" or pos == "s":
            break
        else: print(colored("ERRO: Posição inválida!", "red"))

    PosicaoJogadores[i] = pos

    print(colored("\n--- Alterações ---", "blue"))
    f = f"Trocou a posição do jogador {jog} para {pos}"
    print(f)
    time1 = time.asctime()
    
    historico["hist"].append(f)
    historico["data"].append(time1)

def GerirClassificacoes():
    for i in range(0, len(ListaEquipas)):
        pontos.append(0)
        golos.append(0)
        golosSofridos.append(0)

    for i in range(0, len(ListaEquipas) - 1):
        for j in range(i, len(ListaEquipas) - 1):
            print(f"-------- {ListaEquipas[i]} x {ListaEquipas[j + 1]} --------")
            x = int(input(colored(f"Golos {ListaEquipas[i]}: ", "green")))
            y = int(input(colored(f"Golos {ListaEquipas[j + 1]}: ", "green")))
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

    for i in range(0, len(ListaEquipas)):
        jogosJogados.append(jogos.count(ListaEquipas[i]))

def printarListas():
    print(f"\nEquipas criadas: {ListaEquipas}")
    print(f"Nº de jogadores de cada equipa: {NumJogadoresEquipa}")
    print(f"Jogadores das equipas: {JogadoresDaEquipa}")
    print(f"Posição jogadores: {PosicaoJogadores}")

while True:
    print(colored("\n----- MENU -----", "blue"))
    print("1 - Gerir Equipas")
    print("2 - Gerir Jogos e Classificações")
    print("3 - Histórico de Alterações")
    print("4 - Sair")
    print(colored("----------------", "blue"))

    opcao = int(input(colored("Opção: ", "green")))

    if opcao == 1:
        vez += 1
        if vez == 1 and gerir:
            gerirEquipas()
            gerir = False
            atualizarFicheiro()
        else:
            while True:
                print(colored("\n------ MENU DE GESTÃO DE EQUIPAS ------", "blue"))
                print("1 - Retirar jogador à equipa")
                print("2 - Adicionar jogador à equipa")
                print("3 - Trocar posição do jogador")
                print("4 - Voltar")
                print(colored("---------------------------------------", "blue"))

                g = gerir
                buscarConteudo(g)

                opcao2 = int(input(colored("Opção: ", "green")))

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
                    print(colored("ERRO: Opção inválida!", "red"))

    elif opcao == 2:
        if gerir == False:
            pontos = []
            golos = []
            jogos = []
            classificacoes = []
            golosSofridos = []
            auxiliar = []
            diferenca = []
            info = []

            buscarConteudo(gerir)
            GerirClassificacoes()

            #---------------- Printar Classificações -------------------
            m = max(pontos)
            m2 = min(golosSofridos)
            aux = pontos.count(m)
            pos = pontos.index(m)
            aux2 = golosSofridos.index(m2)

            for i in range(0, len(golos)):
                diferenca.append(golos[i] - golosSofridos[i])

            for i in range(0, len(pontos)):
                if pontos[i] == m:
                    auxiliar.append(diferenca[i])
                else: auxiliar.append(-math.inf)
            
            for x in range(len(ListaEquipas)):
                info.append([])
                for y in range(6):
                    info[x].append(0)

            for i in range(0, len(ListaEquipas)):
                for j in range(0, 6):
                    if j == 0:
                        info[i][j] = ListaEquipas[i]
                    elif j == 1:
                        info[i][j] = jogosJogados[i]
                    elif j == 2:
                        info[i][j] = golos[i]
                    elif j == 3:
                        info[i][j] = golosSofridos[i]
                    elif j == 4:
                        info[i][j] = diferenca[i]
                    elif j == 5:
                        info[i][j] = pontos[i]

            head = ["Equipa", "Nº de Jogos", "Golos", "Golos sofridos", "Diferença de golos", "Pontuação"]
            print(tabulate(info, headers = head, tablefmt = "grid"))

            if aux != 1:
                print(colored(f"Equipa vencedora: {ListaEquipas[auxiliar.index(max(auxiliar))]}", "yellow"))

            else: print(colored(f"Equipa vencedora: {ListaEquipas[pos]}", "yellow"))

        else: print(colored("ERRO: Ainda não criou as equipas!", "red"))

    elif opcao == 3:
        if gerir == False:
            buscarConteudo(gerir)
            if historico["hist"]:
                for i in range(0, len(historico["hist"])):
                    d = historico["data"][i]
                    h = historico["hist"][i]
                    print(f"{h} - {d}")
            else: print(colored("Sem Histórico!", "red"))    
        else: print(colored("Sem Histórico!", "red"))
            

    elif opcao == 4: break

    else: print(colored("\nERRO: Opção não existe!", "red"))
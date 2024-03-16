import time

def perguntarAcao():
    print("\nO que você fará agora?")
    time.sleep(1)
    print("1. Procurar por pistas na floresta.")
    print("2. Conversar com os moradores locais.")
    acao = input("Digite o número correspondente à sua escolha: ")
    return acao

def batalhar():
    print("\nVocê se depara com um inimigo formidável!")
    time.sleep(1)
    print("Escolha seu golpe:")
    print("1. Feitiço de Fogo")
    print("2. Encantamento de Gelo")
    print("3. Raio Mágico")
    golpe = input("Digite o número correspondente ao golpe que você deseja usar: ")

    print("\nEscolha sua defesa:")
    print("1. Escudo Mágico")
    print("2. Barreira de Gelo")
    print("3. Reflexo Arcano")
    defesa = input("Digite o número correspondente à defesa que você deseja usar: ")

    print("\nVocê ataca com um poderoso feitiço!")
    time.sleep(1)
    print("Seu inimigo contra-ataca!")

    if golpe == '1':
        print("Você conjura um Feitiço de Fogo!")
    elif golpe == '2':
        print("Você lança um Encantamento de Gelo!")
    elif golpe == '3':
        print("Você dispara um Raio Mágico!")

    if defesa == '1':
        print("Você conjura um Escudo Mágico para se proteger!")
    elif defesa == '2':
        print("Você ergue uma Barreira de Gelo para bloquear o ataque!")
    elif defesa == '3':
        print("Você utiliza seu Reflexo Arcano para desviar do ataque!")

    print("\nA batalha é intensa, mas você sai vitorioso!")

def historia():
    print("Bem-vindo ao mundo mágico!")
    time.sleep(2)
    print("Você é um jovem bruxo chamado Frodo Potter.")
    time.sleep(2)
    print("Recebe uma carta de Hogwarts, a escola de magia e bruxaria.")
    time.sleep(2)
    print("Decide partir para Hogwarts e embarcar em uma jornada mágica!")
    time.sleep(2)

    escolha1 = input("Aceitar o convite de Hogwarts (digite 'H') ou permanecer na Terra Média (digite 'T')? ").lower()
    
    if escolha1 == 'h':
        print("\nVocê descobre o antigo artefato mágico, o Anel das Trevas, e parte em uma perigosa busca para destruí-lo.")
        time.sleep(2)
        print("Depois de muitas batalhas, enfrenta o Senhor das Trevas em um confronto épico.")
        time.sleep(2)
        print("Com a ajuda de seus amigos, consegue destruir o Anel das Trevas e salvar o mundo da escuridão.")
        time.sleep(2)
        print("Você se torna um herói aclamado, conhecido em toda a Terra Média e Hogwarts.")
    elif escolha1 == 't':
        print("\nVocê decide proteger seu lar da crescente ameaça das trevas.")
        time.sleep(2)
        print("Com o tempo, lidera a resistência contra o avanço das forças das trevas.")
        time.sleep(2)
        print("Reúne um exército de bravos guerreiros e magos e lidera uma batalha final contra o Senhor das Trevas.")
        time.sleep(2)
        print("Depois de uma luta intensa, emerge vitorioso, trazendo a luz de volta à Terra Média.")
        time.sleep(2)
        print("Você se torna uma lenda, lembrada por gerações como o bruxo que salvou a Terra Média.")

    while True:
        acao = perguntarAcao()
        if acao == '1':
            print("\nVocê decide procurar por pistas na floresta.")
            time.sleep(2)
            print("Encontra uma antiga runa mágica escondida sob as raízes de uma árvore.")
            time.sleep(2)
            print("A runa contém um enigma que pode revelar o próximo passo da sua jornada.")
            break
        elif acao == '2':
            print("\nVocê decide conversar com os moradores locais.")
            time.sleep(2)
            break

    batalhar()

historia()

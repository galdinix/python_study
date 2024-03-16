def menuDeVotos():
    print('1 para Lula')
    print('2 para Aragorn')
    print('3 para Gandalf')
    print('4 para branco')
    print('5 para nulo')

def recebeVotos():
    while True:
        try:
            voto = int(input('Seu voto: '))
            if isValid(voto):
                return voto
        except ValueError:
            print('Ocorreu um erro, tente novamente!')

def isValid(voto):
    return 1 <= voto <= 5   

def apurarVotos(voto): 
    if voto == 1:
        return '1\n 0\n 0\n 0\n 0\n'
    if voto == 2:
        return '0\t 1\t 0\t 0\t\t 0\n'
    if voto == 3:
        return '0\t 0\t 1\t 0\t\t 0\n'
    if voto == 4:
        return '0\t 0\t 0\t 1\t\t 0\n'
    return '0\t 0\t 0\t 0\t\t 1\n'

def CriarOuAbrirAquivo():
    with open("dados_votacao2.txt", "w") as arquivo_txt:
        arquivo_txt.write('Opção\t votos\n A\n B\n C\n Branco\n Nulo\n')
        cont = 0
        while cont < 1:
            voto = recebeVotos()
            linha = (f'{apurarVotos(voto)}')
            arquivo_txt.write(linha)
            cont += 1
        print('Arquivo de texto gerado com sucesso')

def main():  
    menuDeVotos()
    CriarOuAbrirAquivo()

main()
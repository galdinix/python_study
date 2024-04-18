def receberPalavras():
    while True:
        try:
            palavra = input('Informe uma palavra')
            if isValid(palavra):
                return palavra
        except ValueError:
            print('Ocorreu um erro, tente novamente!')

def isValid(palavra):
    if len(palavra) == 0:
        return False
    return True

def verificarSePalavraCurtaOuLonga(palavra):
    if len(palavra) < 5:
        return 'curta'
    return 'longa'

def obterRespostaContinuar():
    while True:
        try:
            continuar = int(input('\n\nTecle 0 para verificar outra palavra e qualquer outro número para sair: '))
            return continuar
        except Exception as e:
            print('Ocorreu um erro')

def main():
    while True:
        palvara = receberPalavras()
        tamanho_palavra = verificarSePalavraCurtaOuLonga(palvara)
        print(f' A palavra {palvara} é {tamanho_palavra}!')
        continuar = obterRespostaContinuar()
        if continuar != 0:
            return

main()
        
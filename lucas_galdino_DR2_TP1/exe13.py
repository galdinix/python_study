def receberPalavras():
    while True:
        try:
            palavra = input('Informe uma palavra: ').lower()
            if isValid(palavra):
                return palavra
        except ValueError:
            print('Ocorreu um erro, tente novamente!')

def isValid(palavra):
    if len(palavra) == 0:
        return False
    return True

def verificarSePalindromo(palavra):
    if palavra[::-1] == palavra:
        return 'é palíndromo'
    return 'não é palíndromo'

def obterRespostaContinuar():
    while True:
        try:
            continuar = int(input('\n\nTecle 0 para verificar outra palavra e qualquer outro número para sair: '))
            return continuar
        except Exception as e:
            print('Ocorreu um erro')


def main():
    while True:
        palavra = receberPalavras()
        palavra_eh_palindromo = verificarSePalindromo(palavra)
        print(f' A palavra {palavra} {palavra_eh_palindromo}')
        continuar = obterRespostaContinuar()
        if continuar != 0:
            return
    
main()

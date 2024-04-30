import random

def escolha_usuario():
    while True:
        try:
            numero_usuario = int(input('Escolha um número da sorte entre 0 e 100: '))
            if isValid(numero_usuario):
                return numero_usuario
        except ValueError:
            print('Ocorreu um erro. Tente novamente!!!')

def isValid(numero_usuario):
    if numero_usuario < 0 or numero_usuario > 100:
        print('Os números pricisam ser entre 0 e 100. Tente novamente!!!.')
        return False
    return True

def apurar_resultado(numero_usuario, numero_secreto):
    if numero_secreto == numero_usuario:
        return 'é o correto!', True
    if numero_secreto < numero_usuario:
        return 'é maior que o número secreto!', False
    if numero_secreto > numero_usuario:
        return 'é menor que o número secreto!', False

def main():
    numero_secreto = random.randint(0,100)
    #para fins de teste print(numero_secreto)
    ganhou = False
    while ganhou is False:
        numero_usuario = escolha_usuario()
        resultado, ganhou = apurar_resultado(numero_usuario, numero_secreto)
        print(numero_usuario, resultado)

main()
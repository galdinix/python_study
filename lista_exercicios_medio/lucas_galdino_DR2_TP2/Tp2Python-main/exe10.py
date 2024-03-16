from time import sleep
def receberNumBase10():
    while True:
        try:
            numero_base_10 = int(input('Informe um número: '))
            if isValid(numero_base_10):
                return numero_base_10
            print('Erro, tente novamente!\n')
            sleep(1)
        except ValueError:
            print('Erro, tente novamente!')
            sleep(1)

def isValid(numero_base_10):
    if numero_base_10 < 0:
        return False
    return True

def converter_para_binario(numero):
    if numero == 0: #0em bin é 0
        return '0' 
    binario = ''
    while numero > 0:
        resto = numero % 2  #resto da divisão de numeero/2
        binario = str(resto) + binario  #resto à esquerda
        numero = numero // 2  # div truncada por 2 atualizando numero
    return binario

def main():
    numero_base_10 = receberNumBase10()
    num_binario = converter_para_binario(numero_base_10)
    print(f'O número {numero_base_10} em binário é: {num_binario}')

main()
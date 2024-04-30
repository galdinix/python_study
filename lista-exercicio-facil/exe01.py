def receberValores():
    while True:
        try:
            num1 = float(input('Informe um número: '))
            num2 = float(input('Informe outro número: '))
            if isValid(num1, num2):
                return num1, num2
        except ValueError:
            print('Ocorreu um erro. Tente novamente!!!')

def isValid(num1, num2):
    if num1 == 0 or num2 == 0:
        print('Os números informados não podem ser zero. Tente novamente!!!.')
        return False
    return True
        
num1, num2 = receberValores()

# Realizando cálculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisaoInteira = num1 // num2

print(f'Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}\nDivisão inteira: {divisaoInteira}')

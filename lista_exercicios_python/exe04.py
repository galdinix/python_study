def mostrarMenu():
    print("Menu:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
   
def escolherOpcaoMenu():
    while True:
        try:
            opcao = int(input('Informe a opção: '))  
            if isValid(opcao):
                return opcao
        except ValueError:
            print('Ocorreu um erro. Tente novamente!!!')
       
def isValid(opcao):
    if opcao < 0 or opcao > 5:
        print('Digite uma opção válida, entre 1 e 5. Tente novamente!!!.')
        return False
    return True

def receberNumeros():
    while True:
        try:
            num1 = float(input('Informe um número: '))
            num2 = float(input('Informe outro número: '))
            if isNumberValid(num1, num2):
                return num1, num2
        except ValueError:
            print('Ocorreu um erro. Tente novamente!!!')

def isNumberValid(num1, num2):
    if num1 == 0 or num2 == 0:
        print('Os números informados não podem ser zero. Tente novamente!!!.')
        return False
    return True

def realizarOperacao(num1, num2, opcao):
    if opcao == 1:
        return 'Soma', num1+num2
    if opcao == 2:
        return 'Subtracção', num1-num2
    if opcao == 3:
        return 'Multiplicação',num1*num2
    if opcao == 4:
        return 'Divisão', num1/num2
    
def main():
    mostrarMenu()      
    opcao = escolherOpcaoMenu()
    if opcao == 5:
        print('Encerrando programa')
        return
    num1, num2 = receberNumeros()
    tipoOperacao, resultado = realizarOperacao(num1, num2, opcao)
    print(f'O rultado da {tipoOperacao} é: {resultado}')

main()

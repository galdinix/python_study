import re
def romanoParaNumeral(romano):
    num_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral = 0
    valor_anterior = 0
    for i in reversed(romano):
        valor_atual = num_romanos[i]
        if valor_atual < valor_anterior:
            numeral -= valor_atual
        else:
            numeral += valor_atual
        valor_anterior = valor_atual
    return numeral

def numeralParaRomano(numeral):
    num_numeral = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    num_romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    romano = ''
    i = 0
    while numeral > 0:
        for j in range(numeral // num_numeral[i]): 
            romano += num_romanos[i] 
            numeral -= num_numeral[i] 
        i += 1 
    return romano

def receberValores():
    while True:
        try:
            valor = input('Informe o valor a ser convertido: ').upper().strip()
            if isValorValid(valor):
                return valor
            print('Erro, informe apenas números decimais ou romanos')
        except Exception:
            print('Erro, informe apenas números decimais ou romanos')

def isValorValid(valor):
    regex = r'^(?:[IVXLCDM]+|[1-9]\d*)$'
    return bool(re.match(regex, valor))   

def exibirMenu():
     print('1- Romanos para numeral: \n2- Numeral em romanos \n0- Sair')

def receberOpcMenu():
    while True:
        try:
            opc = int(input('Informe a opção: '))
            if isOpcValid(opc):
                return opc
        except ValueError:
            print('Erro, informe uma opção válida')

def isOpcValid(opc):
    if opc >= 0 and opc <= 2:
        return True
    return False

def main():
    while True:
        exibirMenu()
        opc_menu = receberOpcMenu()
        if opc_menu == 0:
            return
        valor = receberValores()
        if opc_menu == 1:
            valor_convertido = romanoParaNumeral(valor)
            print(f'{valor} em numeral é: {valor_convertido}')
            continue
        valor_convertido = numeralParaRomano(int(valor))
        print(f'{valor} em romanos é: {valor_convertido}')
        
main()
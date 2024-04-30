def receberValorDaCompra():
    while True:
        try:
            valor_compra_total = float(input('Informe o valor da compra: '))
            if isValid(valor_compra_total):
                return valor_compra_total
        except ValueError:
            print('Entre com um número!')

def isValid(valor_compra_total):
    if valor_compra_total <= 0:
        print('Informe valores maiores que 0!')
        return False
    return True

def calcularDescontos(valor_compra_total, percentual_desconto):
    desconto = (percentual_desconto*valor_compra_total)/100
    valor_final = valor_compra_total-desconto
    return valor_final 

def aplicarDescontos(valor_compra_total):
    if valor_compra_total >= 100 and valor_compra_total < 200:
        valor_com_desconto = calcularDescontos(valor_compra_total, 10)
        return valor_com_desconto
    if valor_compra_total >= 200:
        valor_com_desconto = calcularDescontos(valor_compra_total, 15)
        return valor_com_desconto
    return valor_compra_total

def main ():
     valor_compra_total = receberValorDaCompra()
     valor_final = aplicarDescontos(valor_compra_total)
     print(f'Valor final da compra: R${valor_final:.2f}')

main()


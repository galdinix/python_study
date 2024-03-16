def verificarSePrimo(num):
    quantidade_primos = 0
    for i in range(1,101):
        if num%i == 0:
            quantidade_primos +=1
    if quantidade_primos > 2:
        return False
    return True

def construirListaNumPrimos(): #cabe discutir se 1 é ou nao primo
    return [i for i in range(2, 101) if verificarSePrimo(i)]

def main():
    numeros_primos = construirListaNumPrimos()
    print(f'\n\n\t\t\t\tLISTA DE NÚMEROS PRIMOS: \n \n{numeros_primos}')

main()


def receberExpoente():
    while True:
        try:
            expoente = int(input('Informe um expoente: '))
            return expoente
        except ValueError:
            print('Erro, tente novamente!')

def calcularPotencia(expoente = 2):
    return 10**expoente

def main():
    expoente = receberExpoente()
    print(f'Potência alterada pelo usuário (10**{expoente}): {calcularPotencia(expoente)}')
    print(f'\nPotência padrão (10**2): {calcularPotencia()}')

main()
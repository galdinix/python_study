from random import randint

def receberQuantasVezesDadoJogado():
    while True:
        try:
            quant_dados_jogado = int(input('Informe quantas vezes o dado foi jogado: '))
            return quant_dados_jogado
        except ValueError:
            print('Erro, tente novamente!')

def calcularMediaDado(lancamento_dados):
    soma =0
    for i in lancamento_dados:
        soma += i
    return soma / len(lancamento_dados)

def verificarFrequencia(lancamento_dados):
    frequencia = {}
    for i in lancamento_dados:
        if i in frequencia:
            frequencia[i] += 1
        else:
            frequencia[i] = 1
    return frequencia

def main():
    quant_dado_jogado = receberQuantasVezesDadoJogado()
    lancamento_dados = [randint(1, 6) for _ in range(quant_dado_jogado)]
    media = calcularMediaDado(lancamento_dados)
    frequencia = verificarFrequencia(lancamento_dados)
    print("Resultados dos lançamentos:")
    print("Lançamentos:", lancamento_dados)
    print("Média dos lançamentos:", media)
    print("Frequência de cada valor:")
    for chave, freq in frequencia.items():
        print(f"O resultado {chave} apareceu: {freq} vezes")


main()

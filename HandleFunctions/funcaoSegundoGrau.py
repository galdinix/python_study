import math
def contruirFuncaoSegundoGrau(primerio_termo):
    return primerio_termo ** 2

def contruirFuncao(primerio_termo):
    return 1/(1 + math.e**(-primerio_termo))

def CriarOuAbrirAquivo(inicio, fim, intervalo):
    with open("dados_funcaoSingMode.txt", "w") as arquivo_txt:
        arquivo_txt.write('x\t f(x)\n')
        primeiro_termo = inicio
        while primeiro_termo <= fim:
            termo_seguinte = contruirFuncao(primeiro_termo)
            linha = "{:.2f} \t {:.2f}\n".format(primeiro_termo, termo_seguinte)
            arquivo_txt.write(linha)
            primeiro_termo += intervalo
        print('Arquivo de texto gerado com sucesso')

def main():
    inicio = -5
    fim = 5
    intervalo = 0.1
    CriarOuAbrirAquivo(inicio, fim, intervalo)

main()

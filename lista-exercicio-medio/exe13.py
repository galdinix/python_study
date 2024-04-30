from collections import Counter
from random import randint
def obterFrequenciaNumeros(numeros): #retorna um dict onde as keys são os números e a frequência deles são os valores
    return  Counter(numeros)

def desenharHistograma(frequencia_numeros): 
    print("Gráfico:")
    for numero in sorted(frequencia_numeros.keys()):
        linha = '*' * frequencia_numeros[numero]
        print(numero , linha)

def main():
    numeros = [randint(1,6) for i in range(50)]
    frequencia_numereos = obterFrequenciaNumeros(numeros)
    desenharHistograma(frequencia_numereos)

main()

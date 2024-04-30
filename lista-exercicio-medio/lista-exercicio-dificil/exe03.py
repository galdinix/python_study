import re

def receberNumeros():
    while True:
        try:
            sequencia_numeros = input('Informe uma sequência de números separado por espaço: ').strip()
            #trocadno , por .
            sequencia_numeros = sequencia_numeros.replace(',', '.')
            if isValid(sequencia_numeros):
                return sequencia_numeros 
            print('error, informe números')
        except Exception:
            print('erro')

def isValid(sequencia_numeros):
    #apenas números e . separados por espaço
    regex = r'^(\d+(\.\d+)?\s+)*\d+(\.\d+)?$'
    # Verifica se a string corresponde ao padrão
    if re.match(regex, sequencia_numeros):
        return True
    return False

def calcularMedia(lista_num_reais):
    return sum(lista_num_reais)/len(lista_num_reais)

def main():
    sequencia_numeros = receberNumeros()
    sequencia_num_formatado = sequencia_numeros.replace(',', '.')
    lista_numeros = sequencia_num_formatado.split()
    lista_num_reais = [float(a) for a in lista_numeros]
    media = calcularMedia(lista_num_reais)
    print(f'Resultado da média: {round(media, 2)}')

main()
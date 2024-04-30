def receberTexto():
    while True:
        texto = input('Informe o texto: ').lower()
        texto_formatado = texto.replace(' ', '')
        if isValid(texto_formatado):
            return texto_formatado       
        print('Insira apenas letras')

def isValid(texto_formatado):
    if not texto_formatado.isalpha():
        return False
    return True

def verificarFrequenciaDeLetras(texto):
    alfabeto = 'aáàãâbcçdeéèêfghiíìîjklmnoóòõôpqrstuúùûvwxyz'
    frequencia_letras= {letra: 0 for letra in alfabeto}
    for caractere in texto:
        if caractere in alfabeto:
            frequencia_letras[caractere]+=1
    frequencia_letras = ordenarDicionario(frequencia_letras, True)
    #quando volta da ordenação, volta uma lista de tuplas, aqui, transfomo em dict novamente
    frequencia_letras = dict(frequencia_letras)
    return frequencia_letras

def ordenarDicionario(dicionario, decrescente = True):
    return sorted(dicionario.items(), key=lambda x: x[1], reverse=decrescente)

def imprimirHistograma(frquencia_letras):
    for letra, frequencia in frquencia_letras.items():
        if frquencia_letras[letra] == 0:
            continue
        print(f'{letra}: {frequencia * "*"}\n')

def main():
    texto = receberTexto()
    frequencia_letras = verificarFrequenciaDeLetras(texto)
    imprimirHistograma(frequencia_letras)

main()
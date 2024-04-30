def receberFrase():
    while True:
        frase = input('Informe a frase: ').lower()
        frase_formatada = frase.replace(' ', '')
        if isValid(frase_formatada):
            return frase_formatada       
        print('Insira apenas letras')

def isValid(frase):
    if not frase.isalpha():
        return False
    return True

def contarVogais(frase):
    vogais = 'aeiouáàãâéèêíìîóòõôúùû'
    quantidade_vogais = 0
    for caractere in frase:
        if caractere in vogais:
           quantidade_vogais+=1
    return quantidade_vogais

def contarConsoantes(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    quantidade_consoantes = 0
    for caractere in frase:
        if caractere in consoantes:
           quantidade_consoantes+=1
    return quantidade_consoantes

def main():
    frase = receberFrase()
    total_vogais = contarVogais(frase)
    total_consoantes = contarConsoantes(frase)
    print(f'Quantidade de vogais: {total_vogais} \nTotal de consoantes: {total_consoantes}')

main()


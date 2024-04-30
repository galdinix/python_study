def receberTexto():
    while True:
        try:
            texto = input('Informe o texto: ').strip()
            if istextoValid(texto):
                return list(texto)
            print('Error')
        except Exception:
            print('Error')

def istextoValid(texto):
    if texto == '':
        return False
    return True

def verificarFrequencia(texto):
    caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?']
    frequencia_caracteres = {'maiusculo': 0, 'minusculo': 0, 'numeros': 0, 'especiais': 0, 'vazio': 0}
    for caractere in texto:
        if caractere.isupper():
            frequencia_caracteres['maiusculo'] += 1
        if caractere.islower():
           frequencia_caracteres['minusculo'] += 1
        if  caractere.isdigit():
            frequencia_caracteres['numeros'] += 1
        if caractere in caracteres_especiais:
           frequencia_caracteres['especiais']+=1
        if caractere == ' ':
            frequencia_caracteres['vazio'] +=1
    return frequencia_caracteres
   
def imprimirResultado(frequencia_caracteres, texto):
    print(f'''{texto}\nMaiusculo: {frequencia_caracteres['maiusculo']}\nMinusculo: {frequencia_caracteres['minusculo']}\nCaracteres Especiais: {frequencia_caracteres['especiais']}\nNumeros: {frequencia_caracteres['numeros']}''')

def main ():
    texto = receberTexto()
    frequencia_caracteres = verificarFrequencia(texto)
    texto = ''.join(texto)
    imprimirResultado(frequencia_caracteres, texto)

main()
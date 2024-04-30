def construirDictMorse():
    return {
        'A': '·—',
        'B': '—···',
        'C': '—·—·',
        'D': '—··',
        'E': '·',
        'F': '··—·',
        'G': '——·',
        'H': '····',
        'I': '··',
        'J': '·———',
        'K': '—·—',
        'L': '·—··',
        'M': '——',
        'N': '—·',
        'O': '———',
        'P': '·——·',
        'Q': '——·—',
        'R': '·—·',
        'S': '···',
        'T': '—',
        'U': '··—',
        'V': '···—',
        'W': '·——',
        'X': '—··—',
        'Y': '—·——',
        'Z': '——··',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U',
        'À': 'A',
        'È': 'E',
        'Ì': 'I',
        'Ò': 'O',
        'Ù': 'U',
        'Â': 'A',
        'Ê': 'E',
        'Î': 'I',
        'Ô': 'O',
        'Û': 'U',
        'Ã': 'A',
        'Õ': 'O',
        'Ç': 'C',
        '0': '—————',
        '1': '·————',
        '2': '··———',
        '3': '···——',
        '4': '····—',
        '5': '·····',
        '6': '—····',
        '7': '——···',
        '8': '———··',
        '9': '————·',
        ',': '——··———',
        '.': '·—·—··—',
    }

def construirDictAlfabeto():
    dict_morse = construirDictMorse()
    dict_invertido = {}
    for chave, valor in dict_morse.items():
        dict_invertido[valor] = chave
    return dict_invertido

def receberTexto():
    texto = input('Informe o texto: ')
    texto_formatado = texto.upper().strip()
    return texto_formatado

def criptografarTexto(texto):
    dict_morse = construirDictMorse()
    texto_criptografado = ""
    for caractere in texto:
        if caractere in dict_morse:
            texto_criptografado += dict_morse[caractere] 
    else: 
         texto_criptografado += ' '
    return texto_criptografado

def descriptografarTexto(texto):
    texto_descriptografado = ''
    citext = ''
    i = 0
    for caractere in texto:
        if caractere != ' ':
            citext += caractere
        else:
            i += 1
            if i == 2:
                texto_descriptografado += ' '
            else:
                dict_morse = construirDictMorse()
                # Verifica se a sequência de pontos e traços está presente no dicionário Morse
                if citext in dict_morse.values():
                    letra = list(dict_morse.keys())[list(dict_morse.values()).index(citext)]
                    texto_descriptografado += letra
                else:
                    # Se a sequência não for encontrada, adicione uma marcação indicando o problema
                    texto_descriptografado += f'[ERRO:{citext}]'
                citext = ''
    return texto_descriptografado

def exibirMenu():
    print('1- Criptografar em morse: \n2- Descriptografar morse em Pt-Br: \n0- Sair')

def receberOpcMenu():
    while True:
        try:
            opc = int(input('Informe a opção: '))
            if isOpcValid(opc):
                return opc
        except ValueError:
            print('Erro, informe uma opção válida')

def isOpcValid(opc):
    if opc >= 0 and opc <= 2:
        return True
    return False
            
def main():
    while True:
        exibirMenu()
        opcMenu = receberOpcMenu()
        if opcMenu == 1:
            texto = receberTexto()
            texto_criptografado = criptografarTexto(texto)
            print(texto_criptografado)
            continue
        if opcMenu == 2:
            texto = receberTexto()
            texto_descriptografado = descriptografarTexto(texto)
            print(texto_descriptografado)
            continue
        return
       
main()

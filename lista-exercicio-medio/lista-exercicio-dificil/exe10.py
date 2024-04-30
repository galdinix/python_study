num_especiais_letras = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?',0, 1, 2, 3, 4, 5, 6, 7, 8, 9,'a', 'á', 'à', 'ã', 'â', 'b', 'c', 'ç', 'd', 'e', 'é', 'ê', 'f', 'g', 'h', 'i', 'í', 'î', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ò', 'õ', 'ô', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù', 'û', 'v', 'w', 'x', 'y', 'z']

def receberTexto():
        texto = input('Informe o texto: ').lower().strip()
        return list(texto)

def exibirMenu():
    print('1- Criptografar em Cifra de césar: \n2- Descriptografar cifra de César em Pt-Br: \n0- Sair')

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

def criptografar(texto):
    for i in range(len(texto)):
        if texto[i] in num_especiais_letras:
            indice_original = num_especiais_letras.index(texto[i])
            indice_novo = (indice_original + 5) % len(num_especiais_letras)
            texto[i] = num_especiais_letras[indice_novo]
    return ''.join(texto)

def descriptografar(texto): 
    for i in range(len(texto)):
        if texto[i] in num_especiais_letras:
            indice_original = num_especiais_letras.index(texto[i])
            indice_novo = (indice_original - 5) % len(num_especiais_letras)
            texto[i] = num_especiais_letras[indice_novo]
    return ''.join(texto)

def main():
     while True:
        exibirMenu()
        opc = receberOpcMenu()
        if opc == 0:
            return
        texto = receberTexto()
        if opc == 1:
            texto_criptografado = criptografar(texto)
            print(f'Texto criptografado: {texto_criptografado}')
            continue
        texto_descriptografado = descriptografar(texto)
        print(f'Texto descriptografado: {texto_descriptografado}')

main()
    
    


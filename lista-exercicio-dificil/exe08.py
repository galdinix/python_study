def receberPalavraSubstituta():
    while True:
        try:
            palavra = input('Informe a palavra substituta: ').strip()
            if isPalavraValid(palavra):
                return list(palavra)
            print('Error')
        except Exception:
            print('Error')

def isPalavraValid(palavra):
    if palavra == '':
        return False
    return True

def alterarTexto(palavra_substituta, texto):
    for i in range(len(texto)):
        if texto[i] == 'mil':
            texto[i] = ''.join(palavra_substituta)
    return ' '.join(texto)

def main():
    texto = 'mil caíram ao seu lado, dez mil à sua esquerda, enquanto ele avançava destemido pelo campo de batalha, seu espírito inquebrável enfrentando a adversidade com coragem e determinação. O estrondo dos canhões ecoava como trovões distantes, mas ele mantinha sua marcha, guiado pela convicção de que a vitória era inevitável.'.split()
    palavra_substituta = receberPalavraSubstituta()
    texto_alterado = alterarTexto(palavra_substituta, texto)
    print(f'Texto alterado: {texto_alterado}')
    
    
main()
def menuDeVotos():
    print('1 para Lula')
    print('2 para Aragorn')
    print('3 para Gandalf')

def recebeVotos():
    while True:
        try:
            voto = int(input('Seu voto: '))
            if isValid(voto):
                return voto
            print('Digite um valor válido!')
        except ValueError:
            print('Ocorreu um erro, tente novamente!')

def isValid(voto):
    if  voto >= 1 and voto <= 3:
        return True
    return False

def obterRespostaContinuar():
    while True:
        try:
            continuar = int(input('\n\nTecle 0 para outro voto e qualquer outro número para encerrar a votação: '))
            return continuar
        except Exception as e:
            print('Ocorreu um erro')

def apurarVotos(votos):
    contagem_votos = {1 : 0, 2: 0, 3: 0} 
    for voto in votos:
        contagem_votos[voto] += 1  
    return contagem_votos

def verificarVencedor(resultado_da_votacao):
    chave_maior_valor = max(resultado_da_votacao, key=resultado_da_votacao.get)
    maior_valor = resultado_da_votacao[chave_maior_valor]
    vencedor = ''
    if chave_maior_valor == 1:
        vencedor = 'Lula'
        return vencedor, maior_valor
    if chave_maior_valor == 2:
        vencedor = 'Aragorn'
        return vencedor, maior_valor
    vencedor = 'Gandalf'
    return vencedor, maior_valor
    
def main():
   votos= []
   continuar = 0
   while continuar == 0:
       menuDeVotos()
       voto = recebeVotos()
       votos.append(voto)
       continuar = obterRespostaContinuar()
   resultado_da_votacao = apurarVotos(votos)
   vencedor, quantidade_votos = verificarVencedor(resultado_da_votacao) 
   print(f'O vencedor, foi, {vencedor}, com {quantidade_votos} votos')
   print(f'\n\nQuantidade de votos no lula: {resultado_da_votacao[1]}, no Aragorn: {resultado_da_votacao[2]}, no Gandalf: {resultado_da_votacao[3]}')
   return
    
main()

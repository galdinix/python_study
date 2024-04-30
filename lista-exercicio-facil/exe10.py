import random

def exibirMenu():
    print('Tecle 1 para breve história dos Vanyar')
    print('Tecle 2 para breve história dos Noldor')
    print('Tecle 3 para breve história dos Teleri')

def construirHistoria(personagens, acoes, locais, caracteristicas, opcao_acao, opcao_caracteristica, opcao_locais, opcao_personagem):
    print(f'\nOs {personagens[opcao_personagem]} são conhecidos como {caracteristicas[opcao_caracteristica]} e estavam presente na {acoes[opcao_acao]} {locais[opcao_locais]}')
        
def obterRespostaContinuar():
    while True:
        try:
            continuar = int(input('\n\nTecle 0 para outra história e qualquer outro número para sair: '))
            return continuar
        except Exception as e:
            print('Ocorreu um erro')

def main():
    personagens = ['Teleri', 'Noldor', 'Vanyar', 'Luquianos' ]
    caracteristicas = ['os mais temidos, fortes e especialistas em geurra','os mais belos dentre os elfos, grandes poetas e tinham cabelos dourados', 'os mais sábios e habilidosos dentre os elfos, com seus cabelos pretos e olhos cinzentos',' construtores de barcos e grandes cantores e são morenos e olhos cinzentos e cabelos prateados' ]
    acoes = ['na marcha para aniquilar','Primeira leva dos elfos na marcha para', 'Segunda leva dos elfos na marcha para', 'A terceira e maior marcha para']
    locais = ['o oeste da terra média.', 'Mordor', 'Gondor', 'Rio de janeiro']
    while True:
        opcao_acao = random.randint(0, 3)
        opcao_caracteristica = random.randint(0,3)
        opcao_locais = random.randint(0, 3)
        opcao_personagem = random.randint(0, 3)
        construirHistoria(personagens, acoes, locais, caracteristicas, opcao_acao, opcao_caracteristica, opcao_locais, opcao_personagem)
        continuar = obterRespostaContinuar()
        if continuar != 0:
            return
        
main()
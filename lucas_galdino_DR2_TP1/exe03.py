def receberNomes():
    while True:
        try:
            primeiro_nome = input('Informe um nome: ')  
            segundo_nome = input('Informe outro nome: ')
            if isValid(primeiro_nome, segundo_nome):
                return primeiro_nome, segundo_nome
        except ValueError:
            print('Ocorreu um erro. Tente novamente!!!')

def isValid(primeiro_nome, segundo_nome):
    if len(primeiro_nome) <= 3 or len(segundo_nome) <= 3:
        print('Os nomes informados não podem ter menos que 4 caracteres. Tente novamente!!!.')
        return False
    return True


def obterIndiceMedio(primeiro_nome, segundo_nome):
    indice_medio_nome1 = len(primeiro_nome) // 2
    indice_medio_nome2 = len(segundo_nome) // 2
    return indice_medio_nome1, indice_medio_nome2

def combinarNomes(primeiro_nome, segundo_nome, indice_medio_nome1, indice_medio_nome2):
    nomes_combinados = primeiro_nome[:indice_medio_nome1] + segundo_nome[indice_medio_nome2:]
    return nomes_combinados

def main():
    primeiro_nome, segundo_nome = receberNomes()
    indice_medio_nome1, indice_medio_nome2 = obterIndiceMedio(primeiro_nome, segundo_nome)
    nomes_combinados = combinarNomes(primeiro_nome, segundo_nome, indice_medio_nome1, indice_medio_nome2)
    print(f'A combinação dos nomes é: {nomes_combinados}')

main()
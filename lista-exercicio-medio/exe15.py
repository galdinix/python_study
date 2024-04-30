import random
import string

def receberTamSenha():
    while True:
        try:
            tamanho_senha = int(input('Informe o tamanho da senha que deseja: '))
            if isValid(tamanho_senha):
                return tamanho_senha
            print('Erro, tente novamente!')
        except ValueError:
            print('Erro, tente novamente!')

def isValid(tamanho_senha):
    if tamanho_senha <=0:
        return False
    return True

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    caracteres_escolhidos = [random.choice(caracteres) for i in range(tamanho)]
    senha = ''.join(caracteres_escolhidos)
    return senha

def main():
    tamanho_senha = receberTamSenha()
    senha = gerar_senha(tamanho_senha)
    print("Senha gerada:", senha)

main()
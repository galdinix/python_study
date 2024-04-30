import random
import string

def receberTamSenha():
    """
    Solicita ao usuário o tamanho desejado para a senha.


    Returns:
        int: O tamanho desejado para a senha.
    """
    while True:
        try:
            tamanho_senha = int(input('Informe o tamanho da senha que deseja: '))
            if isValid(tamanho_senha):
                return tamanho_senha
            print('Erro, tente novamente!')
        except ValueError:
            print('Erro, tente novamente!')


def isValid(tamanho_senha):
    """
    Verifica se o tamanho da senha fornecido é válido.


    Args:
        tamanho_senha (int): O tamanho da senha a ser verificado.


    Returns:
        bool: True se o tamanho da senha for válido, False caso contrário.
    """
    return tamanho_senha > 0


def gerar_senha(tamanho):
    """
    Gera uma senha aleatória com o tamanho especificado.


    Args:
        tamanho (int): O tamanho da senha desejada.


    Returns:
        str: A senha gerada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    caracteres_escolhidos = [random.choice(caracteres) for _ in range(tamanho)]
    senha = ''.join(caracteres_escolhidos)
    return senha


def main():
    """
    Função principal que solicita o tamanho da senha desejada,
    gera a senha correspondente e a imprime.
    """
    tamanho_senha = receberTamSenha()
    senha = gerar_senha(tamanho_senha)
    print("Senha gerada:", senha)


main()



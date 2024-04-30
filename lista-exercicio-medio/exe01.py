def contarNumPositivos(numeros):
    """
    Conta a quantidade de números positivos em uma lista.

    Args:
        numeros (list): Lista de números.

    Returns:
        int: Número de elementos positivos na lista.
    """
    cont = 0
    for i in numeros:
        if i >= 0:
            cont +=1
    return cont

def main():
    """
    Função principal que gera uma lista de números aleatórios e imprime a quantidade de números positivos.
    """
    from random import randint 

    # Gera uma lista de 10 números aleatórios entre -10 e 10
    numeros = [randint(-10, 10) for i in range(10)]

    # Chama a função contarNumPositivos para contar os números positivos na lista
    cont_num_positivos = contarNumPositivos(numeros)

    # Imprime a quantidade de números positivos na lista
    print(f'Quantidade de números positivos: {cont_num_positivos}')

# Chama a função principal para executar o código
main()

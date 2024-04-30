def somarNumeros():
    cont = 1
    soma = 0
    while cont <= 100:
        soma += cont
        cont += 1
    return soma

def main():
    numeros_somados = somarNumeros()
    print(f'A soma de todos os nuémros de 1 a 100 é {numeros_somados}')
   
main()
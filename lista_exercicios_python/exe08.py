def receberIdade():
    while True:
        try:
            idade = int(input('Informe sua idade: '))
            return idade
        except ValueError:
            print('Ocorreu um erro, digite apenas números!')

def main():
    idade = receberIdade()
    if idade < 18:
        print('Você é menor de idade')
        return
    print('Você é maior de idade')

main()
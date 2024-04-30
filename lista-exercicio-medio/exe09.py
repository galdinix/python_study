def receberNumero():
    while True:
        try:
            numero = int(input('Informe um número: '))
            return numero
        except ValueError:
            print('Erro, tente novamente!!!')

def calcularFatorial(num):
    num_fatorial = num
    for i in range(1,num):
        num_fatorial *= (num-i)
    return num_fatorial

def main():
    num = receberNumero()
    num_fatorial = calcularFatorial(num)
    print(num_fatorial)

main()

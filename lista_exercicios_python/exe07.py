def receberAltura():
    while True:
        try:
            altura = float(input('Informe a altura em metros: '))
            if isValid(altura):
                return altura
        except ValueError:
            print('Ocorreu um erro. Tente novamente!!!')

def receberPeso():
    while True:
        try:
            peso = int(input('Informe a peso em kg: '))
            if isValid(peso):
                return peso
        except ValueError:
            print('Ocorreu um erro. Tente novamente!!!')

def isValid(medida):
    if medida <= 0:
        print('Apenas número maiores que 0')
        return False
    return True

def calcularIMC(peso, altura):
    imc = peso/(altura**2)
    return imc

def apurarResultadosImc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    if imc < 35:
        return "Obesidade grau I"
    if imc < 40:
        return "Obesidade grau II (grave)"
    
    return "Obesidade grau III (mórbida)"

def obterRespostaParaContinuar():
    while True:
        try:
            resposta = int(input('Tecle 0 para CONTINUAR ou qualquer outra tecla para encerrar: '))
            if resposta == 0:
                return True
            return False
        except Exception as e:
            print('Ocorreu um erro. Tente novamente!!!')

def main():
    while True:
        altura = receberAltura()
        peso = receberPeso()
        imc = calcularIMC(peso, altura)
        resultado = apurarResultadosImc(imc)
        print(f'Resultado: {resultado}')
        continuar = obterRespostaParaContinuar()
        if continuar is False:
            return

main()
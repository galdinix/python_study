def receberValores():
    while True:
        try:
            tempo_minutos = int(input('Informe um tempo em minutos: '))
            if isValid(tempo_minutos):
                return tempo_minutos
        except ValueError:
            print('Ocorreu um erro. Tente novamente!!!')

def isValid(tempo_minutos):
    if tempo_minutos == 0:
        print('Os números informados não podem ser zero. Tente novamente!!!.')
        return False
    return True

def converterMinutosParaHorasEMinutos(total_em_minutos):
    tempo_horas_decimal = total_em_minutos / 60
    tempo_horas_int = tempo_horas_decimal//1
    tempo_minutos = (tempo_horas_decimal - tempo_horas_int) * 60
    return tempo_horas_int, tempo_minutos

def converterHorasEMinutosParaMinutos(horas, minutos):
    minutos_totais = horas*60 + minutos
    return minutos_totais

total_em_minutos = receberValores()
horas, minutos = converterMinutosParaHorasEMinutos(total_em_minutos)

#Destina-se a reconversão de horas e minutos para minutos. Poderia uasr o valor de total_em_minutos, mas como no enunciado estava "CONVERTER" preferi fazer o calc
minutos_totais = converterHorasEMinutosParaMinutos(horas, minutos)

print(f'{int(horas)} horas e {int(minutos)} minutos\nMinutos totais: {int(minutos_totais)} minutos')

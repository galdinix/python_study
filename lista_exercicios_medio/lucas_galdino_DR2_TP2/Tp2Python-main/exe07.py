def desenharLinha(caractere = '+', extensao = 12):
    linha = caractere * extensao
    return linha

def main():
    print(f'\t\t\t\t\n LINHA PADRÃO\n{desenharLinha()}') #linha padrao sem parâmetros
    print(f'\n\t\t\t\t\n LINHA CUSTOMIZADA\n{desenharLinha("-", 20)}')  #linha padrao sem parâmetros #linha modificada com parâmetros
    
main()
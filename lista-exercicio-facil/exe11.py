import matplotlib.pyplot as plt
from PIL import Image
import os
from random import randint

def receberQuantidadeDeDados():
    while True:
        try:
            quantidade_dados = int(input('Informe a quantidade de dados: '))
            if isValid(quantidade_dados):
                return quantidade_dados
        except ValueError:
            print('Por favor, insira um número inteiro válido.')

def isValid(quantidade_dados):
    return quantidade_dados > 0

def obter_imagens_dos_dados(resultados):
    imagens = []
    for resultado in resultados:
        nome_arquivo = os.path.join("imagens", f"dado_{resultado}.jpg")
        if os.path.exists(nome_arquivo):
            imagem = Image.open(nome_arquivo)
            imagens.append(imagem)
        else:
            print(f"Arquivo de imagem para a face {resultado} não encontrado")
    return imagens

def exibir_faces_dos_dados(imagens):
    if len(imagens) == 1:
        fig, ax = plt.subplots(figsize=(5, 2))
        ax.imshow(imagens[0])
        ax.axis('off')
    else:
        fig, axs = plt.subplots(1, len(imagens), figsize=(10, 2))
        if len(imagens) == 1:  # Se houver apenas uma imagem, transformamos o objeto de eixo em uma lista para facilitar o acesso
            axs = [axs]
        for i, imagem in enumerate(imagens):
            axs[i].imshow(imagem)
            axs[i].axis('off')
    plt.show()

def lancar_dado():
    return randint(1, 6)


quantidade_dados = receberQuantidadeDeDados()
resultados = [lancar_dado() for _ in range(quantidade_dados)]
imagens = obter_imagens_dos_dados(resultados)
exibir_faces_dos_dados(imagens)

from random import randint 
numeros_negativos=[randint(-10, -1) for i in range(6)] #5 num aleatórios negativos
numeros_positivos=[randint(1, 10) for i in range(6)] #5 num aleatórios positivos
numeros_ordenados = numeros_negativos + numeros_positivos #concatenando listas 
numeros_ordenados.sort() #ordenando lista
print(numeros_ordenados)


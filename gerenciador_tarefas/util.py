from datetime import datetime
def receberNomeTarefa():
    while True:
        try:
            titulo = input('Informe o titulo da tarefa: ')
            return titulo
        except Exception:
            print('Erro, tente novamente')

def receberDescricaotarefa():
    while True:
        try:
            descricao = input('Informe a descrição da tarefa: ')
            return descricao
        except Exception:
            print('Erro, tente novamente')

def receberDataTermino():
    while True:
        data_termino = input('Informe o prazo da tarefa (dia-mês-ano): ')
        if isDateValid(data_termino):
            return data_termino
        print('Erro, tente novamente')

def isDateValid(data_termino, formato='%d-%m-%Y'):
    try:
        datetime.strptime(data_termino, formato)
        return True
    except ValueError:
        return False
    
def receberIdTarefa(tarefas):
    while True:
        try:
            id = int(input('Informe o Id da tarefa: '))
            if isIdValid(id, tarefas):
                return id
            print('Erro, tarefa não encontrada. informe um id válido')
        except ValueError:
            print('Erro, informe um número inteiro')

def isIdValid(id, tarefas):
    if id < len(tarefas) and id >= 0: 
        return True
    return False

def buscarTarefa(id, tarefas):
    for i in range(len(tarefas)):
        if (tarefas[i][0] == id):
           return True
    return False

def  receberOpcMenuPrincipal():
    while True:
        try:
            opcao = int(input("Entre com a opção: "))
            if isOpcValid(opcao):
                return  opcao
            print('Infome um número de 0 a 4')
        except ValueError:
            print('Erro, tente novamente')

def isOpcValid(opcao):
    if opcao > 4 or opcao < 0:
        return False
    return True
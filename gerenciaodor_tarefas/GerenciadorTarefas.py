from util import*
from crud import*
from menu import*
FIM = 0
exibirMenu()
opcao = receberOpcMenuPrincipal()
tarefas=[[]]
while (opcao != FIM):
    match (opcao):
        case 1: adicionarTarefa(tarefas)
        case 2: atualizarTarefa(tarefas)
        case 3: excluirTarefa(tarefas)
        case 4: listarTarefas(tarefas)
    exibirMenu()
    opcao = receberOpcMenuPrincipal()
        



    

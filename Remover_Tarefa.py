
def marcar_concluida() :
    tarefa = input("Coloque a tarefa que deseja marcar como concluida")
    if tarefa not in Dic :
        print("A tarefa não foi concluida ou não exite")
        return
    
    listar_tarefas () 
    nome = input("Digite o nome da tarefa que deseja marcar como concluída: ")
    if nome  in Dados:
        concluida = f"{nome} - Concluída"
        posicao = Dados.index(nome)
        Dados[posicao] = concluida
        print("Tarefa marcada como concluída!")

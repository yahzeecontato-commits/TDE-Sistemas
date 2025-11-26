def remover_tarefa():
    ler_tarefas()
    id_tarefa = int(input("Digite o ID da tarefa que você deseja remover: "))
    if id_tarefa in ler_tarefas:
        del tarefas[ler_tarefas]
        print("Tarefa removida!")
    else:
        print("ID não encontrado.")
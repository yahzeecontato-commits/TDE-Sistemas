def ler_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Tarefas existentes:")
        for tarefa in tarefas:
            print(f"{tarefa['id']} - {tarefa['titulo']} - Concluída: {tarefa['concluida']}")

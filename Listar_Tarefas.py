from dic import Dic
tarefas = Dic

def ler_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Tarefas existentes:")
        for id, tarefa in Dic.items():
            print(f"ID: {id}")
            print(f" Nome:   {tarefa['nome']}")
            print(f" Status: {tarefa['status']}")
            print(f" Prazo:  {tarefa['prazo']}")
            print("-" * 30)
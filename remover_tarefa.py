from dic import Dic
#Issais Ferreira

def remover_tarefa():
    if len(Dic) == 0:
        print("Nenhuma tarefa encontrada.")  
    else:
        for id, tarefa in Dic.items():
            print(f"ID: {id}")
            print(f" Nome:   {tarefa['nome']}")
            print(f" Status: {tarefa['status']}")
            print(f" Prazo:  {tarefa['prazo']}")
            print("-" * 30)
        id_tarefa = int(input("Digite o ID da tarefa que você deseja remover: "))
        if id_tarefa in Dic:
            del Dic[id_tarefa]
            print("Tarefa removida!")
        else:
            print("ID não encontrado.")
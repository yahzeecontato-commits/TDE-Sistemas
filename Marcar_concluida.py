from dic import Dic
import Listar_Tarefas
#Cristhian Rezende

def marcar_concluida():
    if len(Dic) == 0:
        print("Nenhuma tarefa encontrada.")
        return
    Listar_Tarefas.ler_tarefas()

    nome=input("Digite o id da tarefa que deseja marcar como concluida: ")

    for id, tarefa in Dic.items():
        if id in Dic:
            tarefa["status"] ="concluída"
            print(f"Tarefa '{nome}' marcada como concluída ")
            return

    print("Tarefa não encontrada..")
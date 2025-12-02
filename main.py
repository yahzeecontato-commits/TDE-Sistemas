import Add_Tarefa
import Editar_Tarefa
import Marcar_concluida
import remover_tarefa
import Listar_Tarefas
#Yahzee Jonas 


while True: 
    print("1- Adicionar Tarefa") #menu interativo para escolha no prompt com numeros
    print("2- Editar Tarefa")
    print("3- Listar Tarefa")
    print("4- Marcar concluida")
    print("5- Remover Tarefa")
    print("6- Sair")

    select = int(input("Digite umas das opções acima: ")) #seleciona uma das opções listadas 
    if select == 1: 
        Add_Tarefa.adicionar_tarefa()
    elif select == 2:
        Editar_Tarefa.editar_tarefa()
    elif select == 3:
        Listar_Tarefas.ler_tarefas()
    elif select == 4:
        Marcar_concluida.marcar_concluida()
    elif select == 5:
        remover_tarefa.remover_tarefa()
    # Importação das funções feitas pelos integrantes do grupo para deixar o codigo principal mais limpo
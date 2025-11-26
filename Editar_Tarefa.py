tarefas={}
proximo_id = 1
def editar_tarefa():   

    try:
        id_tarefa = int(input("\nDigite o ID da tarefa que deseja editar: "))
    except ValueError:
        print("ID inválido.")
        return

    if id_tarefa not in tarefas:
        print("Tarefa não encontrada.")
        return

    print("\nO que deseja editar?")
    print("1 - Nome da tarefa")
    print("2 - Prazo da tarefa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_nome = input("Digite o novo nome da tarefa: ")
        tarefas[id_tarefa]["nome"] = novo_nome
        print ("Nome da tarefa atualizada!")

    elif opcao == "2":
        novo_prazo = input("Digite o novo prazo: ")
        tarefas[id_tarefa]["prazo"] = novo_prazo
        print("Prazo da tarefa atualizado!")

    else:
        print("Opção inválida.")




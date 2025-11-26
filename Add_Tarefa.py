Dic= {}
proximo_id = 1 

def adicionar_tarefa(): 
    global proximo_id 
    nome = input("Digite o nome da tarefa: ") 
    
    for tarefa in Dic.values(): 
        if tarefa["nome"] == nome: print("Essa tarefa já existe,tente adicionar outra!") 
        return 
    
    prazo = input("Digite o prazo da tarefa (ex: 10/29/2026): ") 

    Dic[proximo_id] = { 
        "nome": nome, 
        "status": "pendente", 
        "prazo": prazo 
        } 
    print(f"Tarefa '{nome}' adicionada com sucesso! ID: {proximo_id}") 
proximo_id += 1
proximo_id = 1 


def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return 

def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice + 1}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice, novo_nome):
    tarefas[indice]["tarefa"] = novo_nome
    print(f"Tarefa {indice + 1 } foi atualizada para {novo_nome}")
    return

def completar_tarefa(tarefas, indice):
    tarefas[indice]["completada"] = True
    print(f"Tarefa {indice + 1} foi completada!")
    return

def remover_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram removidas!")
    return

tarefas = []

while True:
    print("\n Menu do Gerenciador de Lista de Tarefas:")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Completar tarefa")
    print("5 - Remover tarefas completadas")
    print("6 - Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice = int(input("Digite o índice da tarefa que deseja atualizar: ")) - 1
        if indice >= 0 and indice <= len(tarefas):
            novo_nome = input("Digite o novo nome da tarefa: ")
            atualizar_nome_tarefa(tarefas, indice, novo_nome)
        else: 
            print("Índice inválido!")
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice = int(input("Digite o índice da tarefa que deseja completar: ")) - 1
        if indice >= 0 and indice <= len(tarefas):
            completar_tarefa(tarefas, indice)
        else:
            print("Índice inválido!")
    elif escolha == "5":
        remover_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)    
    elif escolha == "6":
        break

print("Obrigado por usar o Gerenciador de Lista de Tarefas!")
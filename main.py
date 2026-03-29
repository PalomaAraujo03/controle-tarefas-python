tarefas = []

while True:
    print("\n📋 MENU")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        
        if tarefa == "":
            print("⚠️ Tarefa não pode ser vazia!")
        else:
            tarefas.append(tarefa)
            print("✅ Tarefa adicionada!")

    elif opcao == "2":
        print("\n📌 Lista de tarefas:")
        
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i} - {tarefa}")

    elif opcao == "3":
        indice = input("Digite o número da tarefa: ")

        if indice.isdigit():
            indice = int(indice)

            if 0 <= indice < len(tarefas):
                tarefas.pop(indice)
                print("❌ Tarefa removida!")
            else:
                print("⚠️ Índice inválido!")
        else:
            print("⚠️ Digite um número válido!")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("⚠️ Opção inválida!")

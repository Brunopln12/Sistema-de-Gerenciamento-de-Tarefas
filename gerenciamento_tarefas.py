import sys

tarefas = []

def adicionar_tarefas(descricao, responsavel):
    if not descricao or not responsavel:
        sys.stderr.write("Descrição e responsável não podem ser vazios!\n")
        return "Erro ao adicionar tarefa!"
    
    tarefa = {
        "descricao": descricao,
        "responsavel": responsavel,
    }
    tarefas.append(tarefa)
    return "Tarefa adicionada!!"

def exibir_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa adicionada!\n")
        return
    
    for tarefa in tarefas:
        print("Tarefa: ")
        for chave, valor in tarefa.items():
            print(f"{chave}: {valor}")
        print("\n")

def buscar_tarefa_responsavel(tarefas, responsavel):
    encontrado = False
    for tarefa in tarefas:
        if responsavel in tarefa['responsavel']:
            print("\nTarefa Encontrada: ")
            for chave, valor in tarefa.items():
                print(f"{chave}: {valor}")
            print("\n")
            encontrado = True
    
    if not encontrado:
        sys.stderr.write("\nNenhuma tarefa encontrada!!!\n")
        return None
    
    return tarefa

def buscar_tarefa_descricao(tarefas, descricao):
    encontrado = False
    for tarefa in tarefas:
        if descricao in tarefa['descricao']:
            print("\nTarefa Encontrada: ")
            for chave, valor in tarefa.items():
                print(f"{chave}: {valor}")
            print("\n")
            encontrado = True
    
    if not encontrado:
        sys.stderr.write("\nNenhuma tarefa encontrada!!!\n")
        return None
    
    return tarefa

def buscar_tarefa():
    while True:
        mini_menu_buscar_tarefa = '''
        MENU DE BUSCA
        [r] Busca por Responsável
        [d] Busca pela Descrição
        [x] Sair
        => '''

        mini_selecao = input(mini_menu_buscar_tarefa).lower()

        if mini_selecao == 'r':
            responsavel = input("\nDigite o nome do Responsável pela Tarefa: ")    
            buscar_tarefa_responsavel(tarefas=tarefas, responsavel=responsavel)
        
        elif mini_selecao == 'd':
            descricao = input("\nDigite uma palavra que contenha na Descrição da Tarefa: ")
            buscar_tarefa_descricao(tarefas=tarefas, descricao=descricao)

        elif mini_selecao == 'x':
            break
        
        else:
            sys.stderr.write("\nOpção inválida!!!\n")
            
def atualizar_tarefa():
    while True:
        mini_menu_atualizar_tarefa = '''
        MENU DE ATUALIZAR
        [r] Atualizar Responsável
        [d] Atualizar Descrição
        [x] Sair
        => '''

        mini_selecao = input(mini_menu_atualizar_tarefa).lower()

        if mini_selecao == 'r':
            responsavel = input("Digite o nome do Responsável que você deseja trocar: ")
            tarefa = buscar_tarefa_responsavel(tarefas, responsavel)
            if tarefa:
                novo_responsavel = input("Digite o nome do novo Responsável pela Tarefa: ")    
                tarefa['responsavel'] = novo_responsavel
                print("Responsável atualizado!!!")
        
        elif mini_selecao == 'd':
            descricao = input("Digite uma palavra que contenha na Descrição da Tarefa que você deseja trocar: ")
            tarefa = buscar_tarefa_descricao(tarefas, descricao)
            if tarefa:
                nova_descricao = input("Digite a nova Descrição da Tarefa: ")    
                tarefa['descricao'] = nova_descricao
                print("Descrição atualizada!!!")

        elif mini_selecao == 'x':
            break
        
        else:
            sys.stderr.write("Opção inválida!!!\n")

def excluir_tarefa(tarefas):
    responsavel = input("Digite o nome do Responsável pela Tarefa que você deseja excluir: ")
    buscar_tarefa_responsavel(tarefas, responsavel)
    descricao = input("Digite uma palavra que contenha na Descrição da Tarefa que você deseja excluir: ")
    buscar_tarefa_descricao(tarefas, descricao)  
    valor_remover = {"descricao": descricao, "responsavel": responsavel}
    
    tarefa_encontrada = None
    
    for tarefa in tarefas:
        if all(tarefa.get(chave) == valor for chave, valor in valor_remover.items()):
            tarefa_encontrada = tarefa
            break
    
    if tarefa_encontrada:
        tarefas.remove(tarefa_encontrada)
        print("Tarefa removida com sucesso.")
    else:
        sys.stderr.write("Tarefa não encontrada.\n")
    
    return tarefas

while True:
    menu = '''
    MENU
    [a] Adicionar Tarefas
    [e] Exibir Tarefas
    [b] Buscar tarefas
    [at] Atualizar tarefas
    [ex] Excluir tarefas
    [q] Sair
    => '''

    selecao = input(menu).lower()

    if selecao == 'a':
        descricao = input("\nEscreva a descrição da Tarefa: ")
        responsavel = input("Qual o responsável por essa Tarefa: ")
        print(adicionar_tarefas(descricao=descricao, responsavel=responsavel))
    
    elif selecao == 'e':
        exibir_tarefas(tarefas=tarefas)

    elif selecao == 'b':
        buscar_tarefa()

    elif selecao == 'at':
        atualizar_tarefa()
    
    elif selecao == 'ex':
        excluir_tarefa(tarefas)
    
    elif selecao == 'q':
        print("\nAté a próxima!!! :)\n")
        break

    else:
        sys.stderr.write("\nOpção inválida!!!\n")

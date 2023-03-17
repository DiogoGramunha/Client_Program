import json

def salvar_clientes(file, cliente):
    file.write(json.dumps(cliente)+'\n')
    file.flush()

def abrir_clientes(file, list):
    file.seek(0)
    clientes = file.readlines()
    if clientes != []:
        for line in clientes: list.append(json.loads(line))


def adicionar_cliente(file, ncliente):
    nome = input("Qual é o nome do cliente? ")
    email = input("Qual é o email do cliente? ")
    numero = input("Qual é o numero de telefone do cliente?") 
    salvar_clientes(file, cliente = {'numero-cliente': ncliente, 'nome': nome, 'email': email, 'numero': numero})
    print("Cliente adicionado com sucesso!")

def editar_cliente(file, lista):
    file.seek(0)
    nome = input("Qual é o nome do cliente que procuras?")
    email = input("Qual é o novo email do cliente?")
    numero = input("Qual é o novo numero do cliente?")
    for cliente in lista:
        if cliente['nome'] == nome:
            cliente['email'] = email
            cliente['numero'] = numero
            print("Cliente editado com sucesso")
        file.write(json.dumps(cliente) + '\n')
    print("Cliente não encontrado")

def excluir_cliente(file, lista):
    nome = input("Qual o nome do cliente que pretendes excluir?")
    for cliente in lista:
        if cliente['nome'] == nome:
            lista.remove(cliente)
            print("Cliente removido!")
            break
    file.seek(0)
    file.truncate() # clear file contents
    for cliente in lista:
        file.write(json.dumps(cliente) + '\n')


""" def excluir_cliente(file, lista):
    
    nome = input("Qual o nome do cliente que pretendes excluir?")
    for cliente in lista:
        if cliente['nome'] != nome:       
            file.write(json.dumps(cliente) + '\n')
            print("Cliente removido!") 

        else: print("Cliente não encontrado")
        file.seek(0)
"""
def lista_cliente(clientes):
    print("Clientes existentes:")
    for cliente in clientes:
        print(f"Numero Cliente: {cliente['numero-cliente']}, Nome: {cliente['nome']}, Email: {cliente['email']}, Numero: {cliente['numero']}")

def buscar_cliente(clientes): 
    nome = input("Qual é o nome do cliente que pretendes encontrar?")
    for cliente in clientes:
        if cliente['nome'] == nome:
            print(f"Numero Cliente: {cliente['numero-cliente']}, Nome: {cliente['nome']}, Email:{cliente['email']}, Numero: {cliente['numero']}")
    print("Cliente não encontrado!")

file = open("clientes.txt", "w+")

while(True):

    lista = []
    abrir_clientes(file, lista)
    
    print("1 - Adicionar novo cliente")
    print("2 - Editar cliente")
    print("3 - Ecluir cliente")
    print("4 - Ver lista de clientes")
    print("5 - Pesquisar por cliente")
    print("0 - Sair")
    opcao = int(input("Que opção pretendes escolher?"))

    if opcao == 1:
        if lista == []:
            ncliente = 1
        else :
            ncliente = int(lista[-1]['numero-cliente']) + 1
        adicionar_cliente(file, ncliente)
        abrir_clientes(file, lista)
    elif opcao == 2:
        editar_cliente(file,lista)
    elif opcao == 3:
        excluir_cliente(file, lista)
    elif opcao == 4:
        lista_cliente(lista)
    elif opcao == 5:
        buscar_cliente(lista)
    elif opcao == 0:
        file.close()
        break
def adicionar_contato(contatos, nome, telefone, email):
    contato = {"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": False}
    contatos.append(contato)
    print(f"\n O contato {nome} adicionado!")
    return

def ver_lista_contatos(contatos):
    print("\nLista de Contatos: ")
    for indice, contato in enumerate(contatos, start=1):
        status = "<3" if contato["Favorito"] == True else " " 
        nome_contato = contato["Nome"]
        email_contato = contato["Email"]
        telefone_contato = contato["Telefone"]
        print(f"\n {indice}. [{status}] Nome:{nome_contato} Telefone:{telefone_contato} Email:{email_contato}")
    return

def editar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    info_alteração = int(input("\nAlternativas: \n Nome - 1 \n Telefone - 2 \n Email - 3 \nAlternativa desejada:"))
    if info_alteração == 1:
        novo_nome = input("Digite o novo Nome:")
        contatos[indice_contato_ajustado]["Nome"] = novo_nome
        print(f"Nome atualizado para {novo_nome}")
    elif info_alteração == 2:
        novo_telefone = input("Digite o novo Telefone:")
        contatos[indice_contato_ajustado]["Telefone"] = novo_telefone   
        print(f"Nome atualizado para {novo_telefone}") 
    elif info_alteração == 3:
        novo_email = input("Digite o novo Email:")
        contatos[indice_contato_ajustado]["Email"] = novo_email  
        print(f"Nome atualizado para {novo_email}")
    return

def marcacao_contato(contatos,indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if  contatos[indice_contato_ajustado]["Favorito"] == True:
        contatos[indice_contato_ajustado]["Favorito"] = False
        print(f"Contato {indice_contato} romovido dos favoritos")
    else:
        contatos[indice_contato_ajustado]["Favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito")
    return

def lista_favorito(contatos):
    for contato in contatos:
        if contato["Favorito"] == True:
            contatos_favoritos.append(contato)
    for indice, contato in enumerate(contatos_favoritos, start=1):
        status = "<3" if contato["Favorito"] == True else " " 
        nome_contato = contato["Nome"]
        email_contato = contato["Email"]
        telefone_contato = contato["Telefone"]
        print(f"\n {indice}. [{status}] Nome:{nome_contato} Telefone:{telefone_contato} Email:{email_contato}")
    return

def apagar_contato(contatos, indice_contato):
        indice_contato_ajustato = int(indice_contato) - 1
        contatos.pop(indice_contato_ajustato)
        print("Contato apagado com sucesso!")

contatos = []
contatos_favoritos = [] 

while True:
    print("\n  Agenda de Contatos")
    print("(1). Adicionar um Contato")
    print("(2). Ver Lista de Contato")
    print("(3). Editar um Contato")
    print("(4). Marcar/Desmarcar como favorito")
    print("(5). Ver Lista de Favoritos")
    print("(6). Apagar um Contato")
    print("(7). Sair")

    funcao = int(input("Escolha o número desejado:"))

    if funcao == 1:
        print("\n Informações do Contato: ")
        nome = input("\nDigite o nome:")
        telefone = input("\nDigite o telefone:")
        email = input("\nDigite o email:")
        adicionar_contato(contatos, nome, telefone, email)

    elif funcao == 2:
        ver_lista_contatos(contatos)

    elif funcao == 3:
        ver_lista_contatos(contatos)
        indice_contato = input("\nDigite o contato desejado:")
        editar_contato(contatos, indice_contato)
    
    elif funcao == 4:
        ver_lista_contatos(contatos)
        indice_contato = input("\nEscolha o contato para marcar/desmarcar como favorito:")
        marcacao_contato(contatos, indice_contato)

    elif funcao == 5:
        lista_favorito(contatos)

    elif funcao == 6:
        ver_lista_contatos(contatos)
        indice_contato = input("\nQual contato deseja apagar: ")
        apagar_contato(contatos, indice_contato)

    elif funcao == 7:
        print("Agenda fechada.")
        break
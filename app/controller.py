from service import (
    cadastro_usuario,
    excluir_usuario,
    atualizar_usuario,
    exibir_um_usuario,
    exibir_informacoes_usuarios,
)


def add_usuario(**usuario):
    if "Nome" not in usuario:
        usuario["Nome"] = "Não informado"
    if "Telefone" not in usuario:
        usuario["Telefone"] = "Não informado"
    if "Endereço" not in usuario:
        usuario["Endereço"] = "Não informado"

    try:
        cadastro_usuario(usuario)
        print("Sucesso")
    except Exception as error:
        print(error)


def excluir_usuarios(*ids):
    for id in ids:
        try:
            excluir_usuario(id)
            print("Sucesso")
        except Exception as error:
            print(error)
            raise


def edit_usuario(*ids):
    for dados in ids:
        id = dados[0]
        dados_usuario = dados[1]
        try:
            atualizar_usuario(id, dados_usuario)
            print("Sucesso")
        except Exception as error:
            print(error)


def exibir_alguns_usuarios(*ids):
    for id in ids:
        try:
            exibir_um_usuario(id)
            print("\n")
        except Exception as error:
            print(error)
            print("\n")


def exibir_todos_usuarios():
    try:
        exibir_informacoes_usuarios()
    except Exception as error:
        print(error)

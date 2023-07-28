from module import ler_arquivo, salvar_arquivo


def novo_usuario(novo_usuario: dict):
    print("dado", novo_usuario)
    usuario_formatado = {
        "Nome": "Não informado",
        "Telefone": "Não informado",
        "Endereço": "Não informado",
        "Status": True,
    }
    for chave, valor in novo_usuario.items():
        usuario_formatado[chave] = valor
    return usuario_formatado


class UsuarioJaCadastrado(Exception):
    pass


def cadastro_usuario(dado: dict):
    arquivo: dict = ler_arquivo()
    novo_arquivo: dict = arquivo.copy()
    existe_usuario = False
    próximo_id = len(arquivo) + 1
    for id, usuario in arquivo.items():
        if (
            dado["Nome"] == usuario["Nome"]
            and dado["Telefone"] == usuario["Telefone"]
            and dado["Endereço"] == usuario["Endereço"]
        ):
            if not usuario["Status"]:
                usuario["Status"] = True
                novo_arquivo[id] = usuario
                existe_usuario = True
            else:
                raise UsuarioJaCadastrado(f"Usuario {usuario['Nome']} já cadastrado")

    if not existe_usuario:
        usuario_formatado = novo_usuario(dado)
        novo_arquivo[str(int(próximo_id))] = usuario_formatado
    salvar_arquivo(novo_arquivo)


class ErroExcluirUsuario(Exception):
    pass


def excluir_usuario(id):
    arquivo = ler_arquivo()
    if id not in arquivo:
        raise ErroExcluirUsuario(f"Usuário ID: {id} não encontrado!")

    else:
        arquivo[id]["Status"] = False
        salvar_arquivo(novo_arquivo=arquivo)


class ErroAtualizarUsuario(Exception):
    pass


def atualizar_usuario(id, dados: dict):
    arquivo = ler_arquivo()
    if id not in arquivo:
        raise ErroAtualizarUsuario(f"Usuário ID: {id} não encontrado!")
    else:
        for chave, valor in dados.items():
            arquivo[id][chave] = valor
        salvar_arquivo(novo_arquivo=arquivo)


class ErroInformacaoUsuario(Exception):
    pass


def exibir_um_usuario(id):
    arquivo = ler_arquivo()
    if id not in arquivo:
        raise ErroInformacaoUsuario(f"Usuario ID: {id} não encontrado!")
    else:
        print(
            f"Nome: {arquivo[id]['Nome']}\n"
            f"Telefone: {arquivo[id]['Telefone']}\n"
            f"Endereço: {arquivo[id]['Endereço']}"
        )


def exibir_informacoes_usuarios():
    arquivo: dict = ler_arquivo()
    usuarios_ativos = []
    for id, usuario in arquivo.items():
        if "Status" in usuario and usuario["Status"]:
            ajusta_usuario = {"ID": id, **usuario}
            del ajusta_usuario["Status"]
            usuarios_ativos.append(ajusta_usuario)
    for usuario in usuarios_ativos:
        for chave, valor in usuario.items():
            print(f"{chave}: {valor}")
        print("")

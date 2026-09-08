import json
#       ^ json vai ser usado como banco de dados.
#       ↓ os serve para dar comandos pro sistema operacional
import os

PASTA_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados")
CAMINHO_USUARIOS = os.path.join(PASTA_DADOS, "usuarios.json")
CAMINHO_PERFIS = os.path.join(PASTA_DADOS, "perfis.json")


def garantir_pasta():
    os.makedirs(PASTA_DADOS, exist_ok=True)
#        ^ garante que a pasta de dados existe. 

def ler_json(caminho, padrao):
#                ^ parametros da funcao.
    if not os.path.exists(caminho):
        return padrao
    try:
#                ↓ abre o parametro caminho e le ele.
        with open(caminho, "r", encoding="utf-8") as f:
#                                        ^ interpreta as letras/numeros em utf-8.
            return json.load(f)
#                        ^ transforma o conteudo do json em codigo de python.
    except (json.JSONDecodeError, OSError):
#                    ^ se der erro ele vai executar o codigo em baixo dele.
#                ↓  retorna o parametro padrao.
        return padrao


def escrever_json(caminho, dados):
    garantir_pasta()
    with open(caminho, "w", encoding="utf-8") as f:
#                       ^ ao inves de ler (r) ele vai escrever (w).
        json.dump(dados, f, ensure_ascii=False, indent=2)
#            ^ pega os dados em python e escreve em um arquivo json.


def carregar_usuarios():
    return ler_json(CAMINHO_USUARIOS, [])
#             ^ auto-explicativo.

def salvar_usuarios(usuarios):
    escrever_json(CAMINHO_USUARIOS, usuarios)
#        chama a funcao de escrever as credenciais no json.

def buscar_usuario_por_email(email):
    email = email.lower().strip()
#                   ^ transforma a string em minuscula.
#            ↓ o for serve pra passar por cada usuario no arquivo json
    for usuario in carregar_usuarios():
#                ↓ se o usuario for encontrado ele retorna usuarion, mas caso nao ele retorna none.
        if usuario["email"].lower() == email:
            return usuario
    return None

#                        ↓ o dicionario que guarda as informacoes do usuario.
def adicionar_usuario(usuario_dict):
    usuarios = carregar_usuarios()
    usuarios.append(usuario_dict)
#              ^ adiciona as credenciais na lista ao inves de sobrescrever.
    salvar_usuarios(usuarios)



def carregar_perfis():
    return ler_json(CAMINHO_PERFIS, {})
#                                     ^ faz o codigo retornar o dicionario vazio caso algo de errado.

def salvar_perfis(perfis):
    escrever_json(CAMINHO_PERFIS, perfis)


def salvar_perfil(email, perfil_dict):
    perfis = carregar_perfis()
    perfis[email.lower().strip()] = perfil_dict
    salvar_perfis(perfis)


def buscar_perfil(email):
    return carregar_perfis().get(email.lower().strip())
    #                         ^ serve para pegar apenas o valor associado ao email, ao inves da lista toda.

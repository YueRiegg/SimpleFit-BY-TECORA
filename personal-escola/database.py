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
#                ^ parâmetros da função.
    if not os.path.exists(caminho):
        return padrao
    try:
#                ↓ abre o parâmetro caminho e lê ele.
        with open(caminho, "r", encoding="utf-8") as f:
#                                        ^ interpreta as letras/números em utf-8.
            return json.load(f)
#                        ^ transforma o conteúdo do json em código de python.
    except (json.JSONDecodeError, OSError):
#                    ^ se der erro ele vai executar o código embaixo dele.
#                ↓  retorna o parâmetro padrão.
        return padrao
def escrever_json(caminho, dados):
    garantir_pasta()
    with open(caminho, "w", encoding="utf-8") as f:
#                       ^ ao invés de ler (r) ele vai escrever (w).
        json.dump(dados, f, ensure_ascii=False, indent=2)
#            ^ pega os dados em python e escreve em um arquivo json.
def carregar_usuarios():
    return ler_json(CAMINHO_USUARIOS, [])
#             ^ autoexplicativo.
def salvar_usuarios(usuarios):
    escrever_json(CAMINHO_USUARIOS, usuarios)
#        chama a função de escrever as credenciais no json.
def buscar_usuario_por_email(email):
    email = email.lower().strip()
#                   ^ transforma a string em minúscula.
#            ↓ o for serve pra passar por cada usuário no arquivo json
    for usuario in carregar_usuarios():
#                ↓ se o usuário for encontrado ele retorna usuario, mas caso não ele retorna None.
        if usuario["email"].lower() == email:
            return usuario
    return None
#                        ↓ o dicionário que guarda as informações do usuário.
def adicionar_usuario(usuario_dict):
    usuarios = carregar_usuarios()
    usuarios.append(usuario_dict)
#              ^ adiciona as credenciais na lista ao invés de sobrescrever.
    salvar_usuarios(usuarios)
def carregar_perfis():
    return ler_json(CAMINHO_PERFIS, {})
#                                     ^ faz o código retornar o dicionário vazio caso algo dê errado.
def salvar_perfis(perfis):
    escrever_json(CAMINHO_PERFIS, perfis)
def salvar_perfil(email, perfil_dict):
    perfis = carregar_perfis()
    perfis[email.lower().strip()] = perfil_dict
    salvar_perfis(perfis)
def buscar_perfil(email):
    return carregar_perfis().get(email.lower().strip())
    #                         ^ serve para pegar apenas o valor associado ao email, ao invés da lista toda.

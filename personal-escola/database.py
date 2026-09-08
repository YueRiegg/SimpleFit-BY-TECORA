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
#            ^ pega os dados em python e escreve em

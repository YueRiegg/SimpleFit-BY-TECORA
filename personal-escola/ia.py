import os
from dotenv import load_dotenv
#      ^ nessa linha eu importo a função de carregar um arquivo .env, que contém a API para a IA da groq.
load_dotenv()
#        ↓ transforma a chave numa variável pra ficar mais fácil de usar.
CHAVE_API = os.getenv("GROQ_API_KEY") or os.getenv("gateway")
cliente_ia = None
#    ^ força a criação de uma variável sem valor.
#    ↓ verifica se a chave existe, e se sim ele define a variável vazia para a API.
if CHAVE_API:
#           ↓ importei dentro do if para caso o cliente não possua uma chave, ele não importe a biblioteca para não depender dela.
    from groq import Groq
    cliente_ia = Groq(api_key=CHAVE_API)
def falar(mensagem, pessoa):
    if _cliente_ia is None:
        return (
            "Erro: nenhuma chave de API da Groq foi encontrada.\n"
            "Configure GROQ_API_KEY no arquivo .env (veja .env.example) "
            "para habilitar o chat com IA."
        )
    contexto = f"""
Nome: {pessoa.nome}
Idade: {pessoa.idade}
Altura: {pessoa.altura}
Peso: {pessoa.peso}
Objetivo: {pessoa.objetivo}
Academia: {pessoa.academia}
Dias de treino: {pessoa.diaTreino}
Horários de treino: {pessoa.horarios}
Escola: {pessoa.escola}
Trabalho: {pessoa.trabalho}
"""
    prompt = f"""
Você é um Personal Virtual.
Ajude a pessoa a organizar sua rotina,
treinos, descanso e alimentação equilibrada.
Informações da pessoa:
{contexto}
Não faça dietas restritivas ou recomendações
médicas.
Diga os treinos que a pessoa deve fazer e em que horário de que dia,
baseado no contexto dado.
Seja muito breve, dizendo apenas o necessário.
Mensagem:
{mensagem}
"""
    try:
#                    ↓ simplifica a resposta da IA pra apenas "resposta".
        resposta = cliente_ia.chat.completions.create(
            model="openai/gpt-oss-120b",
#                    ^ modelo da IA.
            messages=[{"role": "user", "content": prompt}],
#                        ^ mostra quem mandou a mensagem e manda o prompt padrão para ele mostrar a dieta e a rotina de treino.
            temperature=0.7,
#                ^ define o quão criativo a IA pode ser (nesse caso tá como meio termo).
            
        )
#                          ↓ é uma lista de possíveis respostas geradas pela IA (o 0 significa que é a primeira).
        return resposta.choices[0].message.content
#                                    ^ pega o conteúdo da resposta.
    except Exception as erro:
        return "Erro na IA: " + str(erro)
#                    ^ em caso de erros, não fazer o sistema todo parar.
def dieta(pessoa):
    mensagem = """
Monte um plano de alimentação equilibrada
para minha rotina.
Separe em:
Café da manhã
Almoço
Lanche
Jantar
Considere meu peso, altura e objetivo, meus horários e minha rotina.
"""
    return falar(mensagem, pessoa)

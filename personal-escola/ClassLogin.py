from ClassCadastro import hash_senha
# ^ herda hash_senha de ClassCadastro
# ↓ herda buscar_usuario_por_email de database
from database import buscar_usuario_por_email
class Login:
    def __init__(self):
        self.usuario_logado = None
    def realizar_login(self, tentativas=3):
        for _ in range(tentativas):
            email = input("Email: ").strip()
            senha = input("Senha: ")
#                          ↓ transformando usuário no email verificado no banco de dados
            usuario = buscar_usuario_por_email(email)
#                        ↓  verificando o usuário e a senha do usuário.
            if usuario and usuario["senha"] == hash_senha(senha):
                print(f"\nLogin concluído com sucesso! Bem-vindo(a), {usuario['nome']}!")
#                           ↓ altera o objeto da classe transformando o login de None para o usuário
                self.usuario_logado = usuario
#                   ↓ encerra o método da classe
                return usuario
#                ↓ caso o if seja ignorado ele vai dar erro
            print("Erro: dados incorretos.\n")
            
        print("Número máximo de tentativas excedido.")
        return None
    def logout(self):
        self.usuario_logado = None
#                ^ define o login do usuário como None.
        print("Logout concluído.")

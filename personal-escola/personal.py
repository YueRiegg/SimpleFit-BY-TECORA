DIAS_SEMANA = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]


class Pessoa:
    def __init__(self, nome, idade, altura, peso, objetivo):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.objetivo = objetivo


class Personal(Pessoa):
    def __init__(self, nome, idade, altura, peso, objetivo):
        super().__init__(nome, idade, altura, peso, objetivo)

        self.academia = "nao"
        self.diaTreino = []
        self.horarios = ""
        self.escola = {}
        self.trabalho = {}

 
    @staticmethod
#        ^ faz nao precisar de um objeto pra executar o metodo.
    def ler_dias(texto):
        return [d.strip().lower() for d in texto.split(",") if d.strip()]
#                     ^ Transforma um texto separado por vírgulas em uma lista limpa, sem espaços, tudo minúsculo e sem itens vazios.
    def configurar_escola(self):
        resposta = input("\nVocê estuda? (sim/nao): ").strip().lower()
        if resposta.startswith("s"):
            dias = input("Em quais dias? (ex: segunda,terca,quarta): ")
            horario = input("Qual o horário das aulas? (ex: 19h-22h): ").strip()
            for dia in self.ler_dias(dias):
                self.escola[dia] = horario
#            ^ passa por cada dia que o usuario colocou e usa a funcao de ler_dias(dias) pra colocar tudo em horario.
    def configurar_trabalho(self):
        resposta = input("\nVocê trabalha? (sim/nao): ").strip().lower()
        if resposta.startswith("s"):
            dias = input("Em quais dias? (ex: segunda,terca,quarta,quinta,sexta): ")
            horario = input("Qual o horário de trabalho? (ex: 08h-17h): ").strip()
            for dia in self.ler_dias(dias):
                self.trabalho[dia] = horario
#            ^ basicamente a mesma coisa de configurar_escola().
    def configurar_academia(self):
        resposta = input("\nVocê treina na academia? (sim/nao): ").strip().lower()
        self.academia = "sim" if resposta.startswith("s") else "nao"

        if self.academia == "sim":
            dias = input("Quais dias você treina? (ex: segunda,quarta,sexta): ")
            self.diaTreino = self.ler_dias(dias)
            self.horarios = input("Qual o horário de treino? (ex: 18h-19h): ").strip()

    def configurar_rotina_completa(self):
        self.configurar_escola()
        self.configurar_trabalho()
        self.configurar_academia()


    def calendario(self):
        print("\n========== CALENDÁRIO ==========")

        for dia in DIAS_SEMANA:
            print("\n" + dia.upper())
#                               ^ faz tudo ficar em maiusuculo
            ocupado = False

            if dia in self.escola:
                print("Escola:", self.escola[dia])
                ocupado = True

            if dia in self.trabalho:
                print("Trabalho:", self.trabalho[dia])
                ocupado = True

            if dia in self.diaTreino:
                print("Academia:", self.horarios)
                ocupado = True

            if not ocupado:
                print("Dia livre")

    mostrar_calendario = calendario


    def to_dict(self):
#        ^ pega o objeto e transforma em dicionario pra json (nosso banco de dados atual)
        return {"nome": self.nome, "idade": self.idade, "altura": self.altura, "peso": self.peso, "objetivo": self.objetivo,
            "academia": self.academia,"diaTreino": self.diaTreino, "horarios": self.horarios, "escola": self.escola, "trabalho": self.trabalho,}

    @classmethod
#        ^ faz o metodo receber a classe mas nao precisar de objeto. diferente do static que faz nao precisar
#                de classe e nem objeto.
#                  
    def from_dict(cls, dados):
#           ^ transforma o dicionario em objeto da classe.
        perfil = cls(dados["nome"], dados["idade"], dados["altura"], dados["peso"], dados["objetivo"])
#         ^ cria um objeto com os dados obrigatorios.
        perfil.academia = dados.get("academia", "nao")
#                ^ caso academia nao exista ele usa "nao"
        perfil.diaTreino = dados.get("diaTreino", [])
#                            ^ arquivo onde ficam os dados
        perfil.horarios = dados.get("horarios", "")
#                                ^ pega o item do arquivo "dados" (nessa linha ele pega os horarios)
        perfil.escola = dados.get("escola", {})
        perfil.trabalho = dados.get("trabalho", {})
#        {} = dicionario vazio
#        [] = lista vazia
#        "" = string vazia
        return perfil

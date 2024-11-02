from controlador.controlador_clientes import ControladorCliente

class TelaCliente:
    def tela_opcoes(self):
        print("-------- CLIENTES ----------")
        print("Escolha a opcao")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("0 - Retornar")

        try:
            opcao = int(input("Escolha a opcao: "))
            return opcao
        except ValueError:
            print("Entrada inválida. Digite um número.")

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        id_cliente = int(input("ID: "))
        filmes_vistos = input("Filmes vistos (separe por vírgula): ").split(",")
        sessoes_aguardando = input("Sessões aguardando (separe por vírgula): ").split(",")
        
        return {
            "nome": nome,
            "cpf": cpf,
            "id_cliente": id_cliente,
            "filmes_vistos": [f.strip() for f in filmes_vistos],
            "sessoes_aguardando": [s.strip() for s in sessoes_aguardando],
        }

    def mostra_cliente(self, dados_cliente):
        print("NOME DO CLIENTE:", dados_cliente["nome"])
        print("CPF DO CLIENTE:", dados_cliente["cpf"])
        print("ID DO CLIENTE:", dados_cliente["id_cliente"])
        print("FILMES VISTOS DO CLIENTE:", ", ".join(dados_cliente["filmes_vistos"]))
        print("SESSOES AGUARDANDO DO CLIENTE:", ", ".join(dados_cliente["sessoes_aguardando"]))
        print("\n")

    def seleciona_cliente(self):
        try:
            id_cliente = int(input("ID do cliente que deseja selecionar: "))
            return id_cliente
        except ValueError:
            print("Entrada inválida. Digite um número.")

    def mostra_mensagem(self, msg):
        print(msg)

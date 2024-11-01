from controlador_clientes import ControladorCliente

class TelaCliente():
    def __init__(self) -> None:
        pass
        
    def tela_opcoes(self):
        print("-------- CLIENTES ----------")
        print("Escolha a opcao")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Cliente")
        print("4 - Excluir Cliente")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        id_cliente = input("ID: ")
        filmes_vistos = input("Filmes vistos: ")
        sessoes_aguardando = input("Sessoes aguardando: ")

        return {"nome": nome, "cpf": cpf, "id_cliente": id_cliente, "filmes_vistos": filmes_vistos, "sessoes_aguardando": sessoes_aguardando}
    
# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_cliente(self, dados_cliente):
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("CPF DO CLIENTE: ", dados_cliente["cpf"])
        print("ID DO CLIENTE: ", dados_cliente["id_cliente"])
        print("FILMES VISTOS DO CLIENTE: ", dados_cliente["filmes_vistos"])
        print("SESSOES AGUARDANDO DO CLIENTE: ", dados_cliente["sessoes_aguardando"])
        print("\n")
        
#fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf


    def mostra_mensagem(self, msg):
        print(msg)
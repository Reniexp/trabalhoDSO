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
        cpf = input("CPF: ")
        while not self.valida_cpf(cpf):
            print("CPF inválido. Digite exatamente 11 dígitos numéricos.")
            cpf = input("CPF (somente números): ")
        id_cliente = int(input("ID: "))

        filmes_vistos = input("Filmes vistos (separe por vírgula ou digite '0' se não houver): ")
        sessoes_aguardando = input("Sessões aguardando (separe por vírgula ou digite '0' se não houver): ")

        
        filmes_vistos_lista = [] if filmes_vistos.strip() == "0" else [f.strip() for f in filmes_vistos.split(",")]
        sessoes_aguardando_lista = [] if sessoes_aguardando.strip() == "0" else [s.strip() for s in sessoes_aguardando.split(",")]

        return {
            "nome": nome,
            "cpf": cpf,
            "id_cliente": id_cliente,
            "filmes_vistos": filmes_vistos_lista,
            "sessoes_aguardando": sessoes_aguardando_lista,
        }

    def mostra_cliente(self, dados_cliente):
        
        filmes_vistos = dados_cliente.get("filmes_vistos", [])
        sessoes_aguardando = dados_cliente.get("sessoes_aguardando", [])

        print("NOME DO CLIENTE:", dados_cliente["nome"])
        print("CPF DO CLIENTE:", dados_cliente["cpf"])
        print("ID DO CLIENTE:", dados_cliente["id_cliente"])
        print("FILMES VISTOS DO CLIENTE:", ", ".join(filmes_vistos) if filmes_vistos else "Nenhum")
        print("SESSOES AGUARDANDO DO CLIENTE:", ", ".join(sessoes_aguardando) if sessoes_aguardando else "Nenhuma")
        print("\n")

    def seleciona_cliente(self):
        try:
            id_cliente = int(input("ID do cliente que deseja selecionar: "))
            return id_cliente
        except ValueError:
            print("Entrada inválida. Digite um número.")

    def mostra_mensagem(self, msg):
        print(msg)

    def valida_cpf(self, cpf):
        if len(cpf) != 11:
            return False
        for caractere in cpf:
            if caractere < '0' or caractere > '9':  # Verifica se cada caractere é numérico
                return False
        return True
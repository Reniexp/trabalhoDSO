class TelaCliente:
    def tela_opcoes(self) -> int:
        opcao_valida = False
        while not opcao_valida:
            print("-------- CLIENTES ----------")
            print("Escolha a opção:")
            print("1 - Incluir Cliente")
            print("2 - Alterar Cliente")
            print("3 - Listar Clientes")
            print("4 - Excluir Cliente")
            print("0 - Retornar")

            opcao = input("Escolha a opção: ")
            try:
                opcao = int(opcao)
                if opcao in [0, 1, 2, 3, 4]:
                    opcao_valida = True
                else:
                    print("Opção inválida! Escolha um número entre 0 e 4.")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")
        return opcao

    def pega_dados_cliente(self) -> dict:
        print("-------- DADOS CLIENTE ----------")
        
        
        nome = input("Nome: ")
        while nome == "":
            print("O nome não pode ser vazio.")
            nome = input("Nome: ")

        
        cpf = input("CPF (somente números): ")
        while not self.valida_cpf(cpf):
            print("CPF inválido. Digite exatamente 11 dígitos numéricos.")
            cpf = input("CPF (somente números): ")
        
        
        id_cliente = input("ID: ")
        while not self.valida_id_cliente(id_cliente):
            print("ID inválido! Deve ser um número inteiro.")
            id_cliente = input("ID: ")
        id_cliente = int(id_cliente)

        
        filmes_vistos = input("Filmes vistos (separe por vírgula ou digite '0' se não houver): ")
        filmes_vistos_lista = [] if filmes_vistos.strip() == "0" else [f.strip() for f in filmes_vistos.split(",")]

        
        sessoes_aguardando = input("Sessões aguardando (separe por vírgula ou digite '0' se não houver): ")
        sessoes_aguardando_lista = [] if sessoes_aguardando.strip() == "0" else [s.strip() for s in sessoes_aguardando.split(",")]

        return {
            "nome": nome,
            "cpf": cpf,
            "id_cliente": id_cliente,
            "filmes_vistos": filmes_vistos_lista,
            "sessoes_aguardando": sessoes_aguardando_lista,
        }

    def mostra_cliente(self, dados_cliente: dict):
        filmes_vistos = dados_cliente.get("filmes_vistos", [])
        sessoes_aguardando = dados_cliente.get("sessoes_aguardando", [])

        print("NOME DO CLIENTE:", dados_cliente["nome"])
        print("CPF DO CLIENTE:", dados_cliente["cpf"])
        print("ID DO CLIENTE:", dados_cliente["id_cliente"])
        print("FILMES VISTOS DO CLIENTE:", ", ".join(filmes_vistos) if filmes_vistos else "Nenhum")
        print("SESSOES AGUARDANDO DO CLIENTE:", ", ".join(sessoes_aguardando) if sessoes_aguardando else "Nenhuma")
        print("\n")

    def seleciona_cliente(self) -> int:
        id_cliente = input("ID do cliente que deseja selecionar: ")
        while not self.valida_id_cliente(id_cliente):
            print("ID inválido. Digite novamente.")
            id_cliente = input("ID do cliente que deseja selecionar: ")
        return int(id_cliente)

    def mostra_mensagem(self, msg: str):
        print(msg)

    def valida_cpf(self, cpf: str) -> bool:
        if len(cpf) != 11:
            return False
        for caractere in cpf:
            if caractere < '0' or caractere > '9':
                return False
        return True

    def valida_id_cliente(self, id_cliente: str) -> bool:
        try:
            int(id_cliente)
            return True
        except ValueError:
            return False

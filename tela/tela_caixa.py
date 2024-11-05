class TelaCaixa:
    def mostrar_opcoes(self):
        print("\n----- Caixa -----")
        print("INGRESSO : R$10.00")
        print("1 - Vender Ingresso")
        print("2 - Mostrar Total de Vendas")
        print("3 - Listar Ingressos Vendidos")
        print("0 - Sair")
        return int(input("Escolha uma opção: "))

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_detalhes_ingresso(self, ingresso):
        print("\n--- Ingresso Vendido ---")
        print(f"ID: {ingresso.id_ingresso}")
        print(f"Filme: {ingresso.filme.titulo}")
        print(f"Sala: {ingresso.sala.numero}")
        print(f"Horário: {ingresso.horario}")

    def pegar_dados_ingresso(self):
        print("\n--- Dados do Ingresso ---")

        valid_id_ingresso = False
        id_ingresso = input("Id do ingresso: ")

        while not valid_id_ingresso:
            try:
                id_ingresso = int(id_ingresso)
            except:
                print("ID É UM VALOR INTEIRO")
                id_ingresso = input("Id do ingresso: ")
                continue
            else:
                valid_id_ingresso = True

        valid_id_sessao = False
        id_sessao = input("Id da sessao: ")

        while not valid_id_sessao:
            try:
                id_sessao = int(id_sessao)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sessao = input("Id do ingresso: ")
                continue
            else:
                valid_id_sessao = True
        
        valid_id_cliente = False
        id_cliente = input("Id do cliente: ")

        while not valid_id_cliente:
            try:
                id_cliente = int(id_cliente)
            except:
                print("ID É UM VALOR INTEIRO")
                id_cliente = input("Id do cliente: ")
                continue
            else:
                valid_id_cliente = True


        assento = input("Qual assento voce deseja: ")
        while assento == "":
            print()
            print("Não pode ser texto vazio")
            assento = input("Qual assento voce deseja: ")

        return {
            "id_ingresso": id_ingresso,
            "id_cliente" : id_cliente,
            "sessao" : id_sessao,
            "assento" : assento
        }

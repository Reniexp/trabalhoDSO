class TelaCaixa:
    def mostrar_opcoes(self):
        print("\n----- Caixa -----")
        print("1 - Vender Ingresso")
        print("2 - Mostrar Total de Vendas")
        print("3 - Listar Ingressos Vendidos")
        print("0 - Sair")
        return int(input("Escolha uma opção: "))

    def pegar_dados_ingresso(self):
        print("\n--- Dados do Ingresso ---")
        id_ingresso = int(input("ID do ingresso: "))
        filme = input("Filme: ")
        sala = input("Sala: ")
        horario = input("Horário: ")
        preco = float(input("Preço do ingresso: "))
        return {
            "id_ingresso": id_ingresso,
            "filme": filme,
            "sala": sala,
            "horario": horario,
            "preco": preco
        }

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_detalhes_ingresso(self, ingresso):
        print("\n--- Ingresso Vendido ---")
        print(f"ID: {ingresso.id_ingresso}")
        print(f"Filme: {ingresso.filme}")
        print(f"Sala: {ingresso.sala}")
        print(f"Horário: {ingresso.horario}")
        print(f"Preço: R$ {ingresso.preco:.2f}")

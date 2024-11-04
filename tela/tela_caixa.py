class TelaCaixa:
    def mostrar_opcoes(self):
        print("\n----- Caixa -----")
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
        print(f"Preço: R$ {ingresso.preco:.2f}")

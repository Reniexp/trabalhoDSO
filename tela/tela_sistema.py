class TelaSistema:
    def menu_principal(self):
        print("\nMenu Principal do Sistema:")
        print("1 - Gerenciar Clientes")
        print("2 - Gerenciar Funcionários")
        print("3 - Gerenciar Filmes")
        print("4 - Gerenciar Salas")
        print("5 - Gerenciar Sessões")
        print("0 - Sair")
        return int(input("Selecione uma opção: "))

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_opcoes(self, opcoes):
        for key, value in opcoes.items():
            print(f"{key} - {value}")

    def seleciona_opcao(self):
        return int(input("Escolha uma opção: "))

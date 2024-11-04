class TelaSistema:
    def tela_opcoes_sistema(self) -> int:
        invalid_input = True
        first_try = True

        while invalid_input:
            if not first_try:
                print("ESCOLHA UM INTEIRO VÁLIDO")
            print("\nMenu Principal do Sistema:")
            print("\t(1) Gerenciar Clientes")
            print("\t(2) Gerenciar Funcionários")
            print("\t(3) Gerenciar Filmes")
            print("\t(4) Gerenciar Salas")
            print("\t(5) Gerenciar Caixa")
            print("\t(6) Gerenciar Sessões")
            print("\t(0) Sair")
            print()
            
            opcao_escolhida = input("Escolha uma opção: ")
            try:
                opcao_escolhida = int(opcao_escolhida)
            except:
                first_try = False
                continue
            else:
                if opcao_escolhida in [0, 1, 2, 3, 4, 5]:
                    invalid_input = False
                else:
                    print("Opção inválida. Por favor, escolha uma das opções listadas.")
                    first_try = False
        return opcao_escolhida

    def mostra_mensagem(self, mensagem: str):
        """Exibe uma mensagem informativa ao usuário."""
        print(mensagem)

    def pega_opcao_valida(self, prompt: str, opcoes_validas: list) -> int:
        """Solicita uma opção válida e retorna o valor selecionado."""
        invalid_input = True
        first_try = True

        while invalid_input:
            if not first_try:
                print("ESCOLHA UM INTEIRO VÁLIDO")
            print(prompt)
            
            opcao_escolhida = input("Escolha uma opção: ")
            try:
                opcao_escolhida = int(opcao_escolhida)
                if opcao_escolhida in opcoes_validas:
                    invalid_input = False
                else:
                    print(f"Opção inválida. Selecione uma das opções: {opcoes_validas}")
                    first_try = False
            except:
                first_try = False
                continue
        return opcao_escolhida

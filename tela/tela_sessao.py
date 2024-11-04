from exceptions.EntradaInvalidaNoPrompt import EntradaInvalidaNoPrompt

class TelaSessao:
    def tela_opcoes_sessao(self) -> int:
        invalidInput = True
        firstTry = True

        while invalidInput:
            if not firstTry:
                print()
                print("ESCOLHA UM INTEIRO VÁLIDO DE 1 A 6")
                print()
    
            print("Tela Sessao")
            print("\t(1) Mostrar Sessoes Disponíveis")
            print("\t(2) Cadastrar Nova Sessao")
            print("\t(3) Mostrar Dados de Sessao")
            print("\t(4) Alterar Sessao")
            print("\t(5) Deletar Sessao")
            print("\t(6) SAIR da Tela Sessao")
            print()
            
            opcao_escolhida = input("Escolha uma opcao: ")
            try:
                opcao_escolhida = int(opcao_escolhida)
                if opcao_escolhida not in [1,2,3,4,5,6]:
                    raise EntradaInvalidaNoPrompt()
            except:
                firstTry = False
                continue
            else:
                invalidInput = False
        return opcao_escolhida
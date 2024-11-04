from exceptions.EntradaInvalidaNoPrompt import EntradaInvalidaNoPrompt

class TelaSala(): 
    def pega_dados_nova_sala(self):
        valid_id = False
        id_sala = input("Id da sala: ")

        while not valid_id:
            try:
                id_sala = int(id_sala)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sala = input("Id da sala: ")
                continue
            else:
                valid_id = True
        
        nomeSala = input("Nome da sala: ")
        while nomeSala == "":
            print("Não pode ser texto vazio")
            nomeSala = input("Nome da sala: ")
        
        valid_capacidade = False
        capacidade = input("Capacidade da sala: ")

        while not valid_capacidade:
            try:
                capacidade = int(capacidade)
            except:
                print("CAPACIDADE É UM VALOR INTEIRO")
                capacidade = input("Capacidade da sala: ")
                continue
            else:
                valid_capacidade = True
        
        return {
            "idSala" : id_sala,
            "nomeSala" : nomeSala,
            "capacidade" : capacidade
        }
    
    def pega_id_valido_sala(self) -> int:
        valid_id = False
        id_sala = input("Id da sala: ")

        while not valid_id:
            try:
                id_sala = int(id_sala)
            except:
                print("ID É UM VALOR INTEIRO")
                id_sala = input("Id da sala: ")
                continue
            else:
                valid_id = True
        return id_sala
    
    def tela_opcoes_sala(self) -> int:
        invalidInput = True
        firstTry = True
 

        while invalidInput:
            if not firstTry:
                print()
                print("ESCOLHA UM INTEIRO VÁLIDO DE 1 A 6")
                print()

            print("Tela Sala")
            print("\t(1) Mostrar Salas Disponíveis")
            print("\t(2) Cadastrar Nova Sala")
            print("\t(3) Mostrar Dados de Sala")
            print("\t(4) Alterar Sala")
            print("\t(5) Deletar Sala")
            print("\t(6) SAIR da Tela da Sala")
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
    
    def pega_dados_atualizar_sala(self):
        nomeSala = input("Nome da sala: ")
        while nomeSala == "":
            print("Não pode ser texto vazio")
            nomeSala = input("Nome da sala: ")
        
        valid_capacidade = False
        capacidade = input("Capacidade da sala: ")

        while not valid_capacidade:
            try:
                capacidade = int(capacidade)
            except:
                print("CAPACIDADE É UM VALOR INTEIRO")
                capacidade = input("Capacidade da sala: ")
                continue
            else:
                valid_capacidade = True
        
        return {
            "nomeSala" : nomeSala,
            "capacidade" : capacidade
        }
    
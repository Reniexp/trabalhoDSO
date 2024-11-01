class TelaFuncionario():
    def tela_opcoes(self):
        print("-------- FUNCIONARIOS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Funcionario")
        print("2 - Alterar Funcionario")
        print("3 - Listar Funcionario")
        print("4 - Excluir Funcionario")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_funcionario(self):
        print("-------- DADOS FUNCIONARIO ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        id_funcionario = input("ID: ")
        cargo = input("Cargo: ")
        salario = input("Salario: ")
        periodo = input("Periodo: ")

        return {"nome": nome, "cpf": cpf, "id_funcionario": id_funcionario, "cargo": cargo, "salario": salario, "periodo": periodo}
    
# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_funcionario(self, dados_funcionario):
        print("NOME DO FUNCIONARIO: ", dados_funcionario["nome"])
        print("CPF DO FUNCIONARIO: ", dados_funcionario["cpf"])
        print("ID DO FUNCIONARIO: ", dados_funcionario["id_funcionario"])
        print("CARGO DO FUNCIONARIO: ", dados_funcionario["cargo"])
        print("SALARIO DO FUNCIONARIO: ", dados_funcionario["salario"])
        print("PERIODO DO FUNCIONARIO: ", dados_funcionario["periodo"])
        print("\n")
        
#fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_funcionario(self):
        cpf = input("CPF do funcionario que deseja selecionar: ")
        return cpf


    def mostra_mensagem(self, msg):
        print(msg)

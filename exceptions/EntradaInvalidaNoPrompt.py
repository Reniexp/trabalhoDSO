class EntradaInvalidaNoPrompt(Exception):
    def __init__(self, entrada_do_user):
        super().__init__(f"Entrada do usuario {entrada_do_user} é invalida")
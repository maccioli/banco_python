from colorama import Fore, Style

class Validacao:
    def __init__(self, clientesDB):
        self.clientesDB = clientesDB

    def listar_clientes(self):
        for cliente in self.clientesDB.cliente_banco:
            print(f"Conta: {cliente['conta']} Cliente: {cliente['nome']}\n")

    def adicionar_nova_conta(self):
        quantidade_clientes = len(self.clientesDB.cliente_banco)
        if quantidade_clientes < 1:
            return 1
        else:
            return quantidade_clientes + 1

    def verifica_cpf_existente(self, cpf_cliente):
        for cliente in self.clientesDB.cliente_banco:
            while cliente['cpf'] == cpf_cliente:
                print("\n - Ja existe um cadastro com este CPF\n")
                cpf_cliente = input("- Digite o CPF (apenas números): ")

    def localiza_conta_cliente(self, conta_cliente, tipo):
        for cliente in self.clientesDB.cliente_banco:
            if cliente['conta'] == conta_cliente:
                print(f"{tipo} na conta de {cliente['nome']}\n")
                resposta = input(" confirma?(s/n)")
                if resposta == "s":
                    return True
                else:
                    return False
        print(f"\n - {Fore.RED}Conta não encontrada\n {Style.RESET_ALL}")
        return False

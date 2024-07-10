from operacoes import Operacoes
from validacao import Validacao
from tabela_clientes import TabelaClientes
from clientesDB import ClientesDB
from colorama import Fore, Style

class Banco:
    def __init__(self):
        self.clientesDB = ClientesDB()
        self.operacoes = Operacoes(self.clientesDB)
        self.validacao = Validacao(self.clientesDB)
        self.tabela_clientes = TabelaClientes()

    def menu(self):
        menu = """
        ## Bem vindo ao Banco Digital ##

        Escolha uma opção:

        [c] Cadastrar cliente
        [l] Listar clientes
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [v] Saldo
        [q] Sair

        => """.strip()

        while True:
            opcao = input(menu)

            if opcao == "c":
                self.cadastrar_cliente()
            elif opcao == "l":
                self.listar_clientes()
            elif opcao == "d":
                self.depositar()
            elif opcao == "s":
                self.sacar()
            elif opcao == "e":
                self.ver_extrato()
            elif opcao == "v":
                self.ver_saldo()
            elif opcao == "q":
                print("\nObrigado por usar o Banco Digital. Até a próxima!\n")
                break
            else:
                print("\nOperação inválida, por favor selecione novamente a operação desejada.\n")

    def cadastrar_cliente(self):
        conta_cliente = self.validacao.adicionar_nova_conta()
        nome_cliente = input(f"- Digite o nome do cliente: ")
        nascimento_cliente = input("- Digite a data de nascimento (DDMMAAAA): ")
        cpf_cliente = input("- Digite o CPF (apenas números): ")
        self.validacao.verifica_cpf_existente(cpf_cliente)
        endereco_cliente = input("- Digite o endereço: ")
        saldo_cliente = 0
        extrato_cliente = []
        self.operacoes.cadastrar(conta_cliente, nome_cliente, nascimento_cliente, cpf_cliente, endereco_cliente, saldo_cliente, extrato_cliente)

    def listar_clientes(self):
        print(f"\n")
        self.tabela_clientes.print_tabela()
        print(f"\n")

    def depositar(self):
        tipo = "deposito"
        conta_cliente = int(input(f"- Digite a conta para depósito: "))

        if self.validacao.localiza_conta_cliente(conta_cliente, tipo):
            valor = float(input(f"- Digite o valor a ser depositado: "))
            self.operacoes.depositar(conta_cliente, valor, tipo)
        else:
            print(f"{Fore.YELLOW}- Reinicie a operação\n {Style.RESET_ALL}")

    def sacar(self):
        tipo = "saque"
        conta_cliente = int(input(f"- Digite a conta para saque: "))
        if self.validacao.localiza_conta_cliente(conta_cliente, tipo):
            valor = float(input(f"\n - Digite valor a ser sacado(Limite 3 saques/dia e R$500,00/saque): "))
            self.operacoes.sacar(conta_cliente, valor, tipo)
        else:
            print(f"{Fore.YELLOW}- Reinicie a operação\n {Style.RESET_ALL}")

    def ver_extrato(self):
        tipo = 'extrato'
        conta_cliente = int(input(f"- Digite a conta: "))
        if self.validacao.localiza_conta_cliente(conta_cliente, tipo):
            self.operacoes.ver_extrato(conta_cliente)
        else:
            print(f"{Fore.YELLOW}- Reinicie a operação\n {Style.RESET_ALL}")

    def ver_saldo(self):
        tipo = 'saldo'
        conta_cliente = int(input(f"- Digite a conta: "))
        if self.validacao.localiza_conta_cliente(conta_cliente, tipo):
            self.operacoes.ver_saldo(conta_cliente)
        else:
            print(f"{Fore.YELLOW}- Reinicie a operação\n {Style.RESET_ALL}")

if __name__ == "__main__":
    banco = Banco()
    banco.menu()

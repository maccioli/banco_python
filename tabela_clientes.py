import json

class TabelaClientes:
    titulo = "Clientes Banco Digital"
    colunas = ["Nome", "Conta", "Saldo"]

    def __init__(self):
        self.lista = self.constroi_dados()

    def print_tabela(self):
        print(f"{self.titulo.center(50)}\n")
        for coluna in self.colunas:
            print(f"{coluna.ljust(20)}", end="")
        print("")
        print("-" * 20 * len(self.colunas))

        for linha in self.lista:
            for valor in linha:
                print(f"{str(valor).ljust(20)}", end="")
            print("")

    def reload_dados(self):
        with open('clientes.json', 'r') as arquivo:
            return json.load(arquivo)

    def constroi_dados(self):
        dados = []
        clientes = self.reload_dados()
        for cliente in clientes:
            dados.append([cliente['nome'], cliente['conta'], cliente['saldo']])
        return dados

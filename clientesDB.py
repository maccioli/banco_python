import json
import os

class ClientesDB:
    LIMITE_SAQUES = 3
    limite = 500
    numero_saques = 0

    def __init__(self):
        self.cliente_banco = self.carregar_clientes()

    def carregar_clientes(self):
        if not os.path.exists("clientes.json"):
            with open("clientes.json", "w") as arquivo:
                json.dump([], arquivo)
        try:
            with open("clientes.json", "r") as arquivo:
                return json.load(arquivo)
        except json.decoder.JSONDecodeError:
            return []

    def salvar_clientes(self, clientes):
        with open("clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo)

    def adicionar_cliente(self, cliente):
        self.cliente_banco.append(cliente)
        self.salvar_clientes(self.cliente_banco)

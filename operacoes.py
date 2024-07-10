class Operacoes:
    def __init__(self, clientesDB):
        self.clientesDB = clientesDB

    def cadastrar(self, conta_cliente, nome_cliente, nascimento_cliente, cpf_cliente, endereco_cliente, saldo_cliente, extrato_cliente):
        cliente = {
            "conta": conta_cliente,
            "nome": nome_cliente,
            "nascimento": nascimento_cliente,
            "cpf": cpf_cliente,
            "endereco": endereco_cliente,
            "saldo": saldo_cliente,
            "extrato": extrato_cliente
        }
        self.clientesDB.adicionar_cliente(cliente)

    def depositar(self, conta_cliente, valor, tipo):
        for cliente in self.clientesDB.cliente_banco:
            if cliente['conta'] == conta_cliente:
                cliente['saldo'] += valor
                transacao = {"tipo": tipo, "valor": valor}
                cliente['extrato'].append(transacao)
                self.clientesDB.salvar_clientes(self.clientesDB.cliente_banco)
                print(f"\n - Depósito de R${valor:.2f} realizado com sucesso para {cliente['nome']}.\n")

    def sacar(self, conta_cliente, valor, tipo):
        for cliente in self.clientesDB.cliente_banco:
            if cliente['conta'] == conta_cliente:
                if (cliente['saldo'] >= valor and valor > 0 and valor <= self.clientesDB.limite and 
                    self.clientesDB.numero_saques <= self.clientesDB.LIMITE_SAQUES):
                    cliente['saldo'] -= valor
                    transacao = {"tipo": tipo, "valor": valor}
                    cliente['extrato'].append(transacao)
                    self.clientesDB.numero_saques += 1
                    print(f"\n - Saque de R${valor:.2f} realizado com sucesso para {cliente['nome']}.\n")
                else:
                    print("\n - Saque não permitido, verifique o valor digitado, saldo ou limite de saques.\n")
        self.clientesDB.salvar_clientes(self.clientesDB.cliente_banco)

    def ver_extrato(self, conta_cliente):
        for cliente in self.clientesDB.cliente_banco:
            if cliente['conta'] == conta_cliente:
                print(f"\n{cliente['conta']}\n{cliente['nome']}\nExtrato: \n{cliente['extrato']}\n")

    def ver_saldo(self, conta_cliente):
        for cliente in self.clientesDB.cliente_banco:
            if cliente['conta'] == conta_cliente:
                print(f"\n - O saldo de {cliente['nome']} é de: R${cliente['saldo']:.2f}\n")

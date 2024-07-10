import clientesDB

class Cliente:
    def __init__(self, conta_cliente, nome_cliente, nascimento_cliente, cpf_cliente, endereco_cliente, saldo_cliente=0, extrato_cliente=None):
        print("Cadastrando cliente...")
        if extrato_cliente is None:
            extrato_cliente = []
        self.cliente = {
            "conta": conta_cliente, 
            "nome": nome_cliente, 
            "nascimento": nascimento_cliente, 
            "cpf": cpf_cliente, 
            "endereco": endereco_cliente, 
            "saldo": saldo_cliente, 
            "extrato": extrato_cliente
        }

    def depositar(self, valor, clientesDB):
        for cliente in clientesDB.cliente_banco:
            if cliente['conta'] == self.conts_cliente['conta']:
                saldo_cliente = cliente['saldo']
                saldo_cliente += valor
                cliente['saldo'] = saldo_cliente
                
                transacao = {"tipo": tipo, "valor": valor}
                cliente['extrato'].append(transacao)
                
                clientesDB.salvar_clientes(clientesDB.cliente_banco)
                print(f"\n - Depósito de R${valor:.2f} realizado com sucesso para {cliente['nome']}.\n")

    def sacar(self, valor, tipo):
        for cliente in clientesDB.cliente_banco:
            if cliente['conta'] == self.conta_cliente:
                if cliente['saldo'] >= valor and valor > 0 and valor <= clientesDB.limite and clientesDB.numero_saques <= clientesDB.LIMITE_SAQUES:
                    saldo_cliente = cliente['saldo']
                    saldo_cliente -= valor
                    cliente['saldo'] = saldo_cliente

                    transacao = {"tipo": tipo, "valor": valor}
                    cliente['extrato'].append(transacao)    
                    print(f"\n - Saque de {cliente['nome']} no valor de R${valor:.2f} realizado com sucesso.\n")            
                else:
                    print("\n - Saque não permitivo, verifique o valor digitado, saldo ou limite de saques.\n")

        clientesDB.salvar_clientes(clientesDB.cliente_banco)
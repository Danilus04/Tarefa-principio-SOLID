class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def obter_detalhes(self):
        return f"Cliente: {self.nome}"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente  # Dependência direta da classe Cliente

    def exibir_pedido(self):
        detalhes_cliente = self.cliente.obter_detalhes()
        return f"Pedido realizado por: {detalhes_cliente}"


# Exemplo de uso
cliente = Cliente("João")
pedido = Pedido(cliente)
print(pedido.exibir_pedido())


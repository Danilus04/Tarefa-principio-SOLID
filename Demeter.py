class Endereco:
    def __init__(self, rua):
        self.rua = rua

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco

    def get_endereco(self):
        # Método para acessar o endereço do cliente
        return self.endereco

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente

    def imprimir_endereco_entrega(self):
        # Violação do Princípio de Deméter: acessa objeto do objeto do objeto
        print("Entregar na rua:", self.cliente.endereco.rua)

    def imprimir_endereco_entrega_corrigido(self):
        # Correção: acessa o endereço através de um método do cliente
        endereco = self.cliente.get_endereco()
        print("Entregar na rua:", endereco.rua)

if __name__ == "__main__":
    endereco = Endereco("Rua A")
    cliente = Cliente(endereco)
    pedido = Pedido(cliente)
    
       
    pedido.imprimir_endereco_entrega()

    pedido.imprimir_endereco_entrega_corrigido()

   
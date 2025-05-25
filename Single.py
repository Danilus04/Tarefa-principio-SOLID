class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.valor = 0

    def salvar_no_banco(self, valor):
        self.valor += valor
        # Simula o salvamento no banco de dados
        print(f"Salvando {self.valor} no banco de dados...")

class UsuarioCorrigido: 
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.valor = 0

    def salvar_no_banco(self, valor):
        self.valor += valor
        # Simula o salvamento no banco de dados
    
    def informar_valor(self):
        print(f"{self.valor} no banco de dados...")

if __name__ == "__main__":
    usuario = Usuario("João", "Joao@email,com")
    usuario.salvar_no_banco(100)   

    UsuarioCorrigido = UsuarioCorrigido("João", "Joao@email,com")
    UsuarioCorrigido.salvar_no_banco(100) 
    UsuarioCorrigido.informar_valor()
class Usuario:
    def __init__ (self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    def getNome(self): return self.nome
    def getEmail(self): return self.email
    def getSenha(self): return self.senha
    def setNome(self, nome): self.nome = nome
    def setEmail(self, email): self.email = email
    def setSenha(self, senha): self.senha = senha
    def usuario(): pass
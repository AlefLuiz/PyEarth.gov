class Usuario:
    def __init__ (self, nivel_acesso, nome, email, senha, digitais):
        self.nivel_acesso = nivel_acesso
        self.nome = nome
        self.email = email
        self.senha = senha
        self.digitais = digitais
    def getNivelAcesso(self): return self.nivel_acesso
    def getNome(self): return self.nome
    def getEmail(self): return self.email
    def getSenha(self): return self.senha
    def getDigitais(self): return self.digitais
    def setNome(self, nivel_acesso): self.nivel_acesso = nivel_acesso
    def setNome(self, nome): self.nome = nome
    def setEmail(self, email): self.email = email
    def setSenha(self, senha): self.senha = senha
    def setDigital(self, digital): self.digitais.append(digital)
    def usuario(): pass
    
class Pessoa:

    # Construtor
    def __init__(self, nome, idade): # Aqui entra os parametros de construção;
        self.nome = nome
        self.idade = idade # Aqui atribuimos o valor a instância que recebemos dos parametros acima;

    # Métodos
    def alterarNome(self, nome):
        self.nome = nome

    def logar_sistema(self):
        print(f'{self.nome} Esta Longado no Sistema')

# Criamos uma nova instância
p1 = Pessoa('Lucas', 20)

print(p1.nome) # Printando o nome da instância;
p1.alterarNome('Jorge') # Alterando o nome da instância p1 através de um método.
print(p1.nome) # Printando o novo nome

# Executa um método de Instancia que nao precisa de paramentro:
p1.logar_sistema()
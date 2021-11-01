# Classe sempre inicia com letra maiuscula com palavras separadas por CamelCase.
# Funcao sempre minusculo com palavras separadas por underline.

class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

   # Método 
    def logar_sistema(self):
        print(f'{self.nome} Esta Longando no Sistema')

p1 = Pessoas('Caio', 21, '123123123123')

print(p1.nome)
p1.logar_sistema()

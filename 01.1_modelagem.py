# __init__ = metodo contrutor.
# self = atributo da instancia para referenciar a instancia.
# atencao aos atributos de Classes e aos Atributos de Instancia.

class Pessoas:
    possui_olho = True
    possui_boca = False
    raca = 'Humana'

    # Método Construtor
    def __init__(self, nome, idade, cpf):
        print (f'{nome} | {idade} | {cpf} ')

   # Método
    def logar_sistema(self):
        print(f'{self.nome} Esta Longado no Sistema')

# Printa um atributo de instancia.
print(Pessoas.raca)

# Cria uma instancia
p1 = Pessoas('Caio', 21, '123123123123')

# Executa um método da instancia.
p1.logar_sistema


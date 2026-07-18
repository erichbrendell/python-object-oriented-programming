# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    # Dunder Methods
    def __str__(self): 
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: Nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
print(g1)
g1.aniversario()
print(g1)

g2 = Gafanhoto("Mauro", 53)
print(g2)
g2.aniversario()
print(g2)

g3 = Gafanhoto()
print(g3)

# Dunder Attributes
print(g1.__doc__)  
print(g1.__dict__)
print(g2.__dict__)
print(g1.__class__)
print(g2.__class__)

# Dunder Methods
print(g1.__getstate__())
print(g2.__getstate__())

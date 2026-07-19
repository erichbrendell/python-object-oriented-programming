from rich import print
from rich.panel import Panel

class Product:
    """
    Representa um produto.

    Um produto possui um nome e um preço. Além de armazenar
    essas informações, ele pode fornecer uma representação
    textual resumida e gerar o conteúdo de uma etiqueta de preço.
    """

    def __init__(self, nome: str = "Default", preco: float = 0) -> None:
        """
        Inicializa um novo produto.

        Args:
            nome: Nome do produto.
            preco: Preço do produto. O padrão é 0.
        """
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        """
        Retorna uma representação textual resumida do produto.

        Returns:
            Uma string contendo o nome e o preço formatado
            do produto.
        """
        return f"{self.nome} - R${self.preco:,.2f}"

    def etiqueta(self) -> str:
        """
        Retorna o conteúdo da etiqueta de preço.

        Returns:
            Uma string contendo apenas o preço formatado
            do produto.
        """
        return f"R$ {self.preco:,.2f}"

# Instanciação dos objetos
p1 = Product("iPhone 17 Pro Max", 25_000.85)
p2 = Product("Notebook Gamer", 8_000)

# Chamada dos métodos de etiqueta
print(Panel(p1.etiqueta(), title=p1.nome, expand=False))
print(Panel(p2.etiqueta(), title=p2.nome, expand=False))
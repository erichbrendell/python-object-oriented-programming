from rich import print
from rich.panel import Panel

class Churrasco:
    """
    Representa um churrasco e seus custos.

    Com base na quantidade de participantes, calcula a
    quantidade necessária de carne, o custo total e o custo
    por pessoa.
    """

    PRECO_KG_CARNE: float = 82.40
    CARNE_POR_PESSOA: float = 0.4


    def __init__(self, quantidade_pessoas: int) -> None:
        """
        Inicializa um novo churrasco.

        Args:
            quantidade_pessoas: Quantidade de participantes 
                do churrasco.

        Raises:
            ValueError: Se a quantidade de pessoas for menor 
                ou igual a zero.
        """
        if quantidade_pessoas <= 0:
            raise ValueError(
                "A quantidade de pessoas deve ser maior que zero"
            )
        self.quantidade_pessoas = quantidade_pessoas

    def __str__(self) -> str:
        """
        Retorna um relatório textual do churrasco.

        Returns:
            Uma string contendo a quantidade de participantes, 
            o consumo padrão por pessoa, o consumo estimado 
            de carne, o preço da carne por quilograma, o custo 
            total e o custo por pessoa.
        """
        return (
            f"Participantes : {self.quantidade_pessoas}\n"
            f"Consumo/pessoa: {self.CARNE_POR_PESSOA:.1f} kg\n"
            f"Carne         : {self.calcular_total_carne():.1f} kg\n"
            f"Preço/kg      : R$ {self.PRECO_KG_CARNE:.2f}\n"
            f"Custo total   : R$ {self.calcular_custo_total():.2f}\n"
            f"Por pessoa    : R$ {self.calcular_custo_por_pessoa():.2f}"
        )

    def calcular_total_carne(self) -> float:
        """
        Calcula a quantidade total de carne necessária.

        Returns:
            Quantidade de carne em quilogramas.
        """
        return self.quantidade_pessoas * self.CARNE_POR_PESSOA

    def calcular_custo_total(self) -> float:
        """
        Calcula o custo financeiro total do churrasco.

        Returns:
            O valor total baseado na quantidade de 
            carne e no preço por quilo.
        """
        return (
            self.calcular_total_carne() * self.PRECO_KG_CARNE
        )

    def calcular_custo_por_pessoa(self) -> float:
        """
        Calcula o custo do churrasco dividido por participante.

        Returns:
            O valor rateado que cada pessoa deve pagar.
        """
        return (
            self.calcular_custo_total() / self.quantidade_pessoas
        )

    def calcular_custos(self) -> tuple[float, float, float]:
        """
        Retorna um resumo dos cálculos do churrasco.

        Returns:
            Uma tupla contendo:
                - quantidade total de carne (kg);
                - custo total;
                - custo por pessoa.
        """
        return (
            self.calcular_total_carne(),
            self.calcular_custo_total(),
            self.calcular_custo_por_pessoa(),
        )

if __name__ == "__main__":        
    exemplos: list[tuple[str, int]] = [
            ("Churras da TI", 15),
            ("Churras de Fim de Ano", 100),
            ("Confraternização", 35),
        ]

    for titulo, quantidade_pessoas in exemplos:
        churrasco = Churrasco(quantidade_pessoas)
        print(
            Panel(str(churrasco), title=titulo, expand=False)
        )
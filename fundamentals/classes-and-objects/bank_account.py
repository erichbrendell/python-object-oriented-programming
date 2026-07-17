class ContaBancaria:
    """
    Representa uma conta bancária.

    Uma conta bancária possui um identificador, um titular e um saldo,
    além de permitir opeções de depósito e saque.
    """

    def __init__(self, conta_id: int, nome: str, saldo: float = 0) -> None:
        """
        Inicializa uma nova conta bancária.

        Args:
            conta_id: Identificador único da conta.
            nome: Nome do titular da conta.
            saldo: Saldo inicial da conta. O padrão é 0.
        """
        self.conta_id: int = conta_id
        self.titular: str = nome
        self.saldo: float = saldo
        print(f"Conta {self.conta_id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self) -> str:
        """
        Retorna uma representação textual da conta bancária.
        """
        return f"A conta {self.conta_id} de {self.titular} tem R${self.saldo:,.2f} de saldo"

    def depositar(self, valor: float) -> None:
        """
        Realiza um depósito na conta.

        Args:
            valor: Valor a ser depositado.

        Note:
            O depósito somente é realizado se o valor informado for maior que zero.
        """
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:,.2f} autorizado na conta {self.conta_id}")
        else:
            print(f"Depósito de R${valor:,.2f} negado na conta {self.conta_id}: VALOR INVÁLIDO")
    
    def sacar(self, valor: float) -> None:
        """
        Realiza um saque na conta.

        Args:
            valor: Valor a ser sacado.

        Note:
            O saque somente é realizado se houver saldo suficiente.
        """
        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self.conta_id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.conta_id}")


c1 = ContaBancaria(112, "Erich", 3000)
print(c1)
c1.depositar(500)
print(c1)
c1.sacar(2000)
print(c1)
c1.sacar(2_000_000)
c1.depositar(-500)

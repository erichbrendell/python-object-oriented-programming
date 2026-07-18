class Funcionario:
    """
    Representa um funcionário de uma empresa.

    Um funcionário possui nome, setor, cargo e empresa,
    Além de armazenar essas informações, o funcionário 
    pode gerar uma mensagem de apresentação.
    """

    empresa = "Curso em Vídeo"

    def __init__(self, nome: str, setor: str, cargo: str) -> None:
        """
        Inicializa um novo funcionário.

        Args:
            nome: Nome do funcionário.
            setor: Setor onde o funcionário trabalha.
            cargo: Cargo ocupado pelo funcionário.
            empresa: Nome da empresa. O padrão é "Curso em Vídeo".
        """
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self) -> str:
        """
        Retorna uma representação textual resumida do funcionário.

        Returns:
            Uma string contendo uma representação resumida do
            funcionário com seu nome, cargo, setor e empresa.
        """
        return f"{self.nome} ({self.cargo} - {self.setor} - {self.empresa})"
    
    def apresentar(self) -> str:
        """
        Retorna uma mensagem de apresentação do funcionário.

        Returns:
            Uma mensagem de apresentação com o nome, cargo,
            setor e empresa.
        """
        return (
            f"Olá, me chamo {self.nome} "
            f"e sou {self.cargo} "
            f"do setor de {self.setor} "
            f"da empresa {self.empresa}."
        )


# Instanciação dos objetos
funcionarios: list[Funcionario] = [
    Funcionario("Erich", "TI", "Analista de SOC JR"),
    Funcionario("Pedro", "TI", "Programador PL"),
    Funcionario("Amanda", "Administração", "Diretora"),
    Funcionario("Carlos", "Contabilidade", "Contador"),
    Funcionario("Maria", "Marketing", "Gerente")
]

# Chamada dos métods de apresentação
for funcionario in funcionarios:
    print(funcionario.apresentar())
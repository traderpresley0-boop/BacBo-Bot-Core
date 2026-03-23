class Estado:
    def __init__(self):
        self.jogos = 0
        self.vitorias = 0
        self.derrotas = 0
        self.sequencia_atual = []  # Últimas rodadas
        self.historico = []        # Histórico completo

    def atualizar(self, resultado):
        """
        Atualiza o estado do robô com o resultado de uma rodada.
        resultado = {"bolinha": "vermelha" ou "preta", "numero": int, "vitoria": True/False}
        """
        self.jogos += 1
        if resultado.get("vitoria"):
            self.vitorias += 1
        else:
            self.derrotas += 1

        # Atualiza histórico completo
        self.historico.append(resultado)

        # Atualiza sequência recente (últimas 10 rodadas)
        self.sequencia_atual.append(resultado)
        if len(self.sequencia_atual) > 10:
            self.sequencia_atual.pop(0)

    def percentual_vitorias(self):
        if self.jogos == 0:
            return 0
        return (self.vitorias / self.jogos) * 100

    def percentual_derrotas(self):
        if self.jogos == 0:
            return 0
        return (self.derrotas / self.jogos) * 100

    def resetar(self):
        """Reseta o estado para iniciar nova sessão."""
        self.jogos = 0
        self.vitorias = 0
        self.derrotas = 0
        self.sequencia_atual = []
        self.historico = []

    def resumo(self):
        """Retorna um resumo do estado atual."""
        return {
            "jogos": self.jogos,
            "vitorias": self.vitorias,
            "derrotas": self.derrotas,
            "percentual_vitorias": self.percentual_vitorias(),
            "percentual_derrotas": self.percentual_derrotas(),
            "ultima_sequencia": self.sequencia_atual
        }

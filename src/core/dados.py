class Dados:
    def __init__(self):
        self.historico = []

    def obter(self):
        # Retorna um dado simulado da rodada
        rodada = {"bolinha": "vermelha", "numero": 1}
        self.historico.append(rodada)
        return rodada

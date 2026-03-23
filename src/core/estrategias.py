import random

class Estrategias:
    def aplicar(self, rodada):
        """
        Aplica várias estratégias e retorna uma lista de resultados dinâmicos
        baseados na rodada atual.
        """
        resultados = []
        resultados.append(self.rachas(rodada))
        resultados.append(self.alternancia(rodada))
        resultados.append(self.tendencia(rodada))
        resultados.append(self.martingale(rodada))
        resultados.append(self.anti_martingale(rodada))
        resultados.append(self.repeticao(rodada))
        resultados.append(self.probabilidade_combinada(rodada))
        resultados.append(self.adaptativo_risco(rodada))
        resultados.append(self.espelho(rodada))
        resultados.append(self.contraria(rodada))
        resultados.append(self.media_movel(rodada))
        resultados.append(self.pico_sequencia(rodada))
        resultados.append(self.aleatoria_ponderada(rodada))
        resultados.append(self.volatilidade(rodada))
        resultados.append(self.correlacao_numeros(rodada))
        return resultados

    # Estratégias dinâmicas de exemplo
    def rachas(self, rodada):
        if rodada["bolinha"] == "vermelha":
            return {"estrategia": "rachas", "acao": "apostar"}
        return {"estrategia": "rachas", "acao": "esperar"}

    def alternancia(self, rodada):
        # Alterna aposta se número é ímpar/par
        if rodada["numero"] % 2 == 0:
            return {"estrategia": "alternancia", "acao": "apostar"}
        return {"estrategia": "alternancia", "acao": "esperar"}

    def tendencia(self, rodada):
        # Exemplo simplificado: aposta em vermelho sempre
        return {"estrategia": "tendencia", "acao": "apostar"}

    def martingale(self, rodada):
        return {"estrategia": "martingale", "acao": "apostar"}

    def anti_martingale(self, rodada):
        return {"estrategia": "anti_martingale", "acao": "apostar"}

    def repeticao(self, rodada):
        return {"estrategia": "repeticao", "acao": "apostar"}

    def probabilidade_combinada(self, rodada):
        return {"estrategia": "probabilidade_combinada", "acao": "apostar"}

    def adaptativo_risco(self, rodada):
        return {"estrategia": "adaptativo_risco", "acao": "apostar"}

    def espelho(self, rodada):
        return {"estrategia": "espelho", "acao": "apostar"}

    def contraria(self, rodada):
        return {"estrategia": "contraria", "acao": "apostar"}

    def media_movel(self, rodada):
        return {"estrategia": "media_movel", "acao": "apostar"}

    def pico_sequencia(self, rodada):
        return {"estrategia": "pico_sequencia", "acao": "apostar"}

    def aleatoria_ponderada(self, rodada):
        return {"estrategia": "aleatoria_ponderada", "acao": random.choice(["apostar", "esperar"])}

    def volatilidade(self, rodada):
        return {"estrategia": "volatilidade", "acao": "apostar"}

    def correlacao_numeros(self, rodada):
        return {"estrategia": "correlacao_numeros", "acao": "apostar"}

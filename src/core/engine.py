from src.core.estrategias import Estrategias
from src.core.dados import Dados

class Engine:
    def __init__(self):
        self.dados = Dados()
        self.estrategias = Estrategias()

    def start(self):
        print("Engine iniciada")
        self.rodar()
    
    def rodar(self):
        rodada = self.dados.obter()
        resultados = self.estrategias.aplicar(rodada)
        print("Resultados das estratégias:")
        for r in resultados:
            print(r)

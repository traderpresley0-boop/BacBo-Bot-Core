from src.core.estrategias import Estrategias
from src.core.dados import Dados
from src.core.estado import Estado
from src.core.decisao import decidir

class Engine:
    def __init__(self):
        self.dados = Dados()
        self.estado = Estado()
        self.estrategias = Estrategias()

    def start(self):
        print("Engine iniciada")
        self.rodar()

    def rodar(self):
        rodada = self.dados.obter()  # obtém a rodada simulada
        resultados = self.estrategias.aplicar(rodada)  # aplica todas as estratégias
        acao_final = decidir(resultados)  # decide se aposta ou espera

        # Atualiza o estado do robô
        resultado_rodada = {
            "bolinha": rodada["bolinha"],
            "numero": rodada["numero"],
            "vitoria": acao_final == "apostar"  # simplificação
        }
        self.estado.atualizar(resultado_rodada)

        print("Resultados das estratégias:")
        for r in resultados:
            print(r)
        print("Decisão final:", acao_final)
        print("Resumo do estado:", self.estado.resumo())

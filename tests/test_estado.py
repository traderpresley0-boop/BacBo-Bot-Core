# tests/test_estado.py
from core.estado import atualizar_estado, estado

def test_sequencia():
    atualizar_estado({"valor":"P"})
    atualizar_estado({"valor":"P"})
    atualizar_estado({"valor":"B"})
    assert estado["sequencia_atual"]["tipo"] == "B"
    assert estado["sequencia_atual"]["tamanho"] == 1
    print("Teste de sequências OK!")

if __name__ == "__main__":
    test_sequencia()

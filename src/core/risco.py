def risco_aplicavel(banca, aposta, limite):
    if banca - aposta < limite:
        return False
    return True

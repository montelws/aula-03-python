def reg (nota, boletim=None):
    """Nao altera a lista original. """
    if boletim is None:
        boletim = []
    novo = boletim [:]  # copia da lista
    novo.append(nota)
    return novo

notas = [7]
print (reg(9, notas))    
print (notas)  # [7] 
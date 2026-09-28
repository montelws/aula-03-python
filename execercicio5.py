# script_desafio.py
from class_calculadora import somar, subtrair, multiplicar, dividir
                        
def orc (qtd, preco, frete=0):
    """Total do pedido. """
    s = multiplicar (qtd, preco)
    return somar (s, frete)

print (orc (3, 49.9, 15))

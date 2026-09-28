# procedimento com parametros 
def cabecalho (titulo, largura=30):
    print (titulo.center (largura, '-'))  # centraliza e preenche com '-'
    print ('=' * largura)  # imprime linha de '='

cabecalho ("Relatorio")

# erro comum:
x = cabecalho ("A") + 1 # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
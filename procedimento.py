# procedimento : so executa acao
def saudar (nome):
    print(f'Olá {nome}!') # exibe 
    # nao existe return, entao devolve None

saudar ('Maria')  # Olá Maria!

r = saudar ('João')  # Olá João!
print (r)  # None, pois saudar nao devolve nada
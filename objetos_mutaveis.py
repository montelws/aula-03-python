# lista, dicionario e set : mutaveis

def add (lista, valor):
    lista.append (valor)  # altera a lista original

compras = ["arroz"]
add (compras, "feijao")
print (compras)  # ['arroz', 'feijao']  pois compras

add
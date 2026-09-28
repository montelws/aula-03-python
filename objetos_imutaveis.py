# int, float, str e tupla : imutaveis

def dobrar (numero):
    numero = numero * 2  # novo objeto
    return numero

valor = 10
print(dobrar(valor))  # 20
print(valor)  # 10


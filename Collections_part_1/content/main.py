idades = [1,2,3,4,5,6,7,8,9,10,11,12]

def soma_um(idade):
    return idade + 1

print([(soma_um(idade)) for idade in idades if idade > 3])

# Errado
def faz_processamento(lista = []):
    print(len(lista))
    lista.append("teste")

faz_processamento()
faz_processamento()
faz_processamento()
faz_processamento()


# Correto
def faz_processamento(lista = None):
    if lista is None:
        lista = []
    print(len(lista))
    lista.append("teste")

faz_processamento()
faz_processamento()
faz_processamento()
faz_processamento()

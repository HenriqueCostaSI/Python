"""
ZIP

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares
"""

# Exemplo

lista1 = [1, 2, 3]
lista2 = [3, 4, 5]

zip1 = zip(lista1, lista2)

# Sempre podemos gerar

print(list(zip1))

zip2 = zip(lista1, lista2)  # Temos que reexecutar pois se perde
print(tuple(zip2))

zip3 = zip(lista1, lista2)
print(set(zip3))

zip4 = zip(lista1, lista2)
print(dict(zip4))

lista3 = [1, 2, 3, 4, 5]

zip5 = zip(lista1, lista2, lista3)  # Ele sempre se baseia na menor lista
print(list(zip5))

####################################################################

# Podemos utilizar diferentes iteráveis com zip5

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 1, 'b': 2, 'c': 3}

zt = zip(tupla, lista, dicionario.values())

# Lista de Tuplas
dados = [(1, 2), (3, 4), (5, 6)]

print(list(zip(*dados)))

#########################################################################

# Exemplos mais Complexos

prova1 = [80, 90, 78]
prova2 = [98, 58, 98]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dados[0]: max(dados[1], dado[2] for dados in zip(alunos, prova1, prova2))}

# Podemos utilizar um map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))

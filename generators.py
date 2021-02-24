"""
Generator Expression -> Seriam tuple compheresion

"""
"""

#Poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Daniel']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension

res = [nome[0] for nome in nomes]
print(type(res))

# Generators

res = (nome[0] == 'C' for nome in nomes)
print(type(res))

"""

# Gerando uma lista de números com List Comprehension
from sys import getsizeof  # ->Retorna a quantidade de bytes em memória
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com dic Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generators
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer uma mesma tarefa:')
print(
    f'List Comprehesion: {list_comp}, Set Comprehension: {set_comp}, Dictionary Comprehension: {dic_comp} e Generator: {gen}')

################################

# INTERANDO

gen = (x * 10 for x in range(100))
print(gen)
print(type(gen))

for num in gen:
    print(num)

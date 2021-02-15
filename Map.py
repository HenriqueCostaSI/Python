"""
Map

Com map, fazemos mapeamento de valores para função

"""

import math


def area_c(r):
    return math.pi * (r ** 2)


print(area_c(2))

raios = [2, 5, 7.1, 9.4, 3]
areas = []

# Forma comum
for r in raios:
    areas.append((area_c(r)))

print(areas)

# Forma com Map

# Map recebe a função e depois um iterável

areas = map(area_c, raios)

print(areas)

print(list(areas))

print(type(areas))

# Forma com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a funcao map() ele zera

"""
Para fixar - Map

Temos dados iteráveis:

dados: a1, a1, ..., an

Temos uma funcao: f(x)

# Utilizamos a funcao map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função

#Map object: f(a1), f(a2), ...

"""

# Mais exemplosc

cidades = [('Berlim', 29), ('CAiro', 36),
           ('Buenos Aires', 19), ('Los Angeles', 26)]

# Para f

# f = 9/5 * c + 32

# Lambda


def c_para_f(dado): return (dado[0], (9/5) * dado[1] + 32)


print(list(map(c_para_f, cidades)))


"""
Ordered Dict

# Em um dicionário  a ordem de inderção dos elemtos não é garantida
dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

for chave, valor in dict.items():
    print(f'chave={chave}:valor={valor}')

"""

# Importando

from collections import OrderedDict
dic = orderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})

# Entendo as Diferenças

dict1 = {'a': 1, 'b': 2, 'c': 3}

dict2 = {'a': 1, 'c': 3, 'b': 2}

print(dict1 == dict2)  # Deu True

odict1 = OrderedDict({'a': 1, 'b': 2, 'c': 3})
odict2 = OrderedDict({'a': 1, 'c': 3, 'b': 2})

print(odict1 == odict2)  # Deu False

"""
Trabalhando com Módulos Bultin (módulos integrados, que já vem instalados no Python)

-----------------------------------------------
[Python[Módulos bultin]]
...............................................
"""

# Utilizando alias (apelidos) para módulos/funções

from random import (
    random,
    randint,
    shuffle,
    choice
)
from random import randint as rdi, random as rdm
from random import *
import random as rdm

print(rdm.random())

################################################################


print(random())

################################################################

# Utilizando alias (apelidos) para módulos/funções


print(rdm.rdi(5, 89))

################################################################

# Costumamos a utilizar tuple para múltiplos imports de um mesmo módulo

lista = [1, 2, 3, 4]

shuffle(lista)
print(lista)

print(choice(' Henrique'))

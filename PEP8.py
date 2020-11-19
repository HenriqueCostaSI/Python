"""
PEP8 - Python Enhancement Proposal

A ideia da pep8 é que possamos escrever códigos Python de forma Pythonica

"""

"""
 1) Utilize Camel Case para nomes de Classes
 
"""


class Calculadora:
    pass


class CalculadoraCientifica:
    pass

    """
 2)Utilize nomes em minúsculo, separados por _ para funções e variáveis
 
 """


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impam = 5

"""
3)Utilize 4 espaços para identação

"""

if 'a' in 'banana':
    print('tem')

""" 

4)Separar funções e definições de classe com duas linhas em branco
    -Métodos dentro de uma classe devem ser separardos com uma única linha
    
5) Imports devem ser sempre feitos em linhas separadas
    
"""

# import sys

# caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

"""
from types import (
    StringType
    ListType
    SetType
)
"""

# Imports devem ser colocados no topo do arquivo, logo depois de qualquer comentário ou docstrings e antes de
# constantes e variaveis globais

""" 

6)Espaços em expressões e instruçoes

"""
# fazer

x = 5

"""

7)Termine sempre uma instruções com uma nova linha

"""

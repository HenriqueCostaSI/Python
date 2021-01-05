"""
Funções com retorno


"""
"""
numeros = [1, 2, 3]

ret = numeros.pop()

print(f'Retrono de pop: {ret})

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
Podemos passar a execução de função para outras funções
"""

# Exemplo de função de




from random import random
def quadrado_de_7():
    print(7 * 7)

# Vamos refatorar essa função


def squared_7():
    return 7 * 7


ret_squared = squared_7()

print(f'Retorno {ret_squared}')

# ou

print(f'Retorno {quadrado_de_7()}')

################################

# Exemplo com diferentes returns


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 7
    return 'a'


print(nova_funcao())

################################

# Desempacotamento


def outra_funcao():
    return 1, 2, 3


num1, num2, num3 = outra_funcao()

print(num1, num2, num3)

################################

# Vamos criar uma funcao para jogar uma moeda


def joga_moeda():
    # Gera um número pseudo randômica entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogar_moeda())

################################


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return 'É ímpar'
    else:
        return False

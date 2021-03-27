"""
Utilizando Lambdas

Expressões Lambdas, são funções sem nome, ou seja, funções anônimas.

# Funções em Python 

    

"""

# Funções em Python


def funcao(x):
    return 3 * x


print(funcao(4))

# Expressão Lambda

lambda x: 3 * x

# E como utilizar Lambda


def calc(x): return 3 * x

# Podemos ter expressões lambdas com múltiplas entradas


def nome_completo(nome, sobrenome): return nome.strip().title() + ' ' + sobrenome.strip().title()  # strip. retira os espaços do início e fim da string


print(nome_completo(' Henrique', 'Matheus '))

# Em funções Python podemos ter nenhuma entrada


def amar(): return 'I love Python'


def duas(x, y): return (x * y) ** 0.5


def tres(x, y, z): return (z * 4) + x * y

duas2 = lambda x, y: (x * y) ** 0.5

tres2 = lambda x, y, z:  3/ ( 1/ x+1 / y + 1 / z)

print(duas2(55, 3))

print(tres2(3, 6, 4))


print(tres(2, 34, 54))

################################

autores = ['Isaac Asimov', 'Ray Bradbury',
           'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

################################

# Função Quadrática

# f(x) = a * x **2 + b *x + c


def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = funcao_quadratica(2, 3, -5)

print(teste(0))
print(funcao_quadratica(3, 0, 1)(2))

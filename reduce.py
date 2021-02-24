"""
Reduce

OBS: Não é uma função built-in, temos que importar do módulo 'functools'

99% das vezes um loop for é mais legível

Para entender o reduce():

#Imagine que você tem uma coleção de dados:

dados = [a1,a2, a3, ..., an]

# E você tem uma função que recebe dois parâmetros: a função e o iterável;

def função(x, y):
    return x * yield

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável;

reduce(função, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros dados e guarda o resultado
    Passo 2: res2 = f(res1, a3)
    .
    .
    ..

    Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final, reduce() irá retornar o resultado final

    funcao(funcao(funcao(a1, a2), a3), a4)

"""
from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7]

# Para utilizar o reduce() nós precisamos de uma função que recbe dois parâmetros


def multi(x, y): return x * y


res = reduce(multi, dados)
print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)

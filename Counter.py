"""
Counter -> Recebe um interavel como parâmetro e cria um objeto do tipo Collections Counter, que é parecido com um dicionário, contendo como chave o elemento 
da lista passada como parâmetro e coomo valor a quantidade de ocorrencias desse elemento

Colelections -> High-performance Container Datetypes

"""

# Utilizando o Counter

from collections import Counter

# podemos utilizar qualquer interavel
lista = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 7, 1, 2]

res = Counter(lista)

print(res)
print(type(res))

"""
Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 7: 2, 6: 1})

Para cada elemento da lista o counter criou uma chave e no valor colocou  número de ocorrências

"""
print(Counter('Geek University'))

print(res.most_common(10))

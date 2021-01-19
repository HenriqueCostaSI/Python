"""
Listas alinhadas (Nested Listas)

*Algumas linguagens possuem os arrays: unidimensionais, multidimensionais(Matrizes)

Em Python temos as listas

"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3

print(listas)

print(type(listas))

# Como fazemos para acessar os dados al

print(listas[0][1])  # Acesso linha x coluna -> 2

print(listas[2][1])

# Interando com loops em uma lista alinhada

for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valoer) for valor in lisa] for lista in listas]

# Outros exemplos

# Gerando uma matrix 3x3

matrix = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(matrix)

# Gernado jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(
    1, 4)] for valor in range(1, 4)]

# Gerando valor iniciais

print([['*' for i in range(1, 4)] for valor in range(1, 4)])

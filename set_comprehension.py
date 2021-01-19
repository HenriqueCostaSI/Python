"""
Set Comprehension

"""

# Exmplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo

numeros = {x ** 2 fox x in range(10)}
print(numeros)

# TRansformando em dicionarios

numeros = {x: x ** 2 fox x in range(10)}
print(numeros)

# Para finalizar

letras = {letra for letra in 'Geek University'}
print(letras)

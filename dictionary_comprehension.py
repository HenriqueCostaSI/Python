"""
Diconary Comprehesion

Criando um dicionario 

dicionario = {'a': 1, 'b': 2, 'c': 3}

Sintaxe

{chave:valor for valor in iterável}

"""

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

################################

numeros = [1, 2, 3, 4, 5, 6]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

################################

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chasves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)


# Exemplo com lógica condicional

numeros = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)

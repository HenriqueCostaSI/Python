"""
List Comprehension  

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Síntaxe da List Comprehension 

[ dado for dado in iterável ]

"""

# Exemplos

numeros = [1, 2, 3, 4, 5, 6]

res = [numer * 10 for numero in numero]

print(res)

"""
Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numero
- A segunda parte: numero * 10


"""

res = [numero / 2 for numero in numero]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

###############################################################

# List Comprehension vs Loops

# Loop

numeros = [1, 2, 3, 4, 5, 6]

numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List :Comprehension
print([numero * 2 for numero in numeros])

###############################################################

# Outros exemplos

# 1
nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2


def caixa_alta(nome):
    nome = nome.replaace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'douglas']

print([caixa_alta(amigos) for amigo in amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.13]])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])


################################################################

"""
PARTE 2

Nos podemos adicionar estruturas condicionais lógicas às nossas List Comprehension


"""


# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numeros % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

# Refatorando

# Qualquer número par módulo de 2 é 0 e 0 em Python é FAlse. not False = True

pares = [numero for numero in numeros if not numero % 2]

# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True

ímpares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

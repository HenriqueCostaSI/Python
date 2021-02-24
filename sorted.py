"""
Sorted

Podemos utilizar com qualquer iterável para ordenar.

Retorno-> Sempre uma lista com os elementos ordenados.

"""

# Exemplo

numeros = [45, 56, 34]-

print(sorted(numeros))  # Ordenar do menor para o maior


# Adicionando parâmetros

print(sorted(numeros, reverse=True))  # Ordenar do maior para o menor

############################################################

# Convertendo

print(tuple(sorted(numeros)))  # Ordenar do menor para o maior
print(set(sorted(numeros)))  # Ordenar do menor para o maior

############################################################

usuarios = [
    {"username": "Samuel423", "tweets": [
        "Eu sou de esquerda", "Apoio o Psol"]},
    {"username": "Carla23", "tweets": ["Eu sou de direita", "Apoio o Psc"]},
    {"username": "Miguellll", "tweets": [], "cor": "amarelo"},
    {"username": "Dogface", "tweets": []}

]

# Ordenando por username
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

############################################################

# Último exemplo de

musicas = [
    {"título": "Giz", "Tocou": 123043}
    {"título": "Índios", "Tocou": 4329535}
    {"título": "Eu Sei", "Tocou": 2535432}
    {"título": "Onde Anda Você", "Tocou": 1345324}
]

# Ordenando da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["Tocou"]))

# Ordenando da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["Tocou"], reverse=True))

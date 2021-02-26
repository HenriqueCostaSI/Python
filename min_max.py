"""
Min e Maximum

max()-> Retorna o maior valor em um interável ou o maior de dois ou mais elementos

"""

#Exemplo 
lista = [1, 5, 8, 24, 4543]
print(max(lista))

tupla = (1, 5, 8, 24, 4543)
print(max(tupla))

set = {1, 5, 8, 24, 4543}
print(max(set))

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5 }
print(max(dicionario))
print(max.values(dicionario))


################################################################

#Um programa que recebe dois dados do usuário para

val1= int(input('Informe o primeiro valor: '))

val2= int(input('Informe o segundo valor: '))

print(max(val1, val2))

##################################################################

"""
min()-> Retorna o menor valor em um interável ou o menor de dois ou mais elementos
"""

#Exemplo 
lista = [1, 5, 8, 24, 4543]
print(min(lista))

tupla = (1, 5, 8, 24, 4543)
print(min(tupla))

set = {1, 5, 8, 24, 4543}
print(min(set))

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5 }
print(min(dicionario))
print(min.values(dicionario))

####################################################################

# Outros exemplos

nomes = ['Ana', 'Camila', 'Eduardo', 'Daniel']

print(max(nomes))# Daniel
print(min(nomes))# Ana

print(max(nomes, key=lambda nome: len(nome)))# Eduardo
print(min(nomes, key=lambda nome: len(nome)))# Ana

##################################

musicas = [
    {"título": "Giz", "Tocou": 123043}
    {"título": "Índios", "Tocou": 4329535}
    {"título": "Eu Sei", "Tocou": 2535432}
    {"título": "Onde Anda Você", "Tocou": 1345324}
]

print(max(musicas, key=lambda musica: musica['Tocou']))# A que mais tocou
print(min(musicas, key=lambda musica: musica['Tocou']))# A que menos Tocou

print(max(musicas, key=lambda musica: musica['Tocou'])['titulo'])# A que mais tocou só o título
print(min(musicas, key=lambda musica: musica['Tocou'])['titulo'])# A que menos Tocou só o título

# Desafio! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda

max = 0

for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == max:
        print(musica['Tocou'])


min = 9999999999999999999

for musica in musicas:
    if musica['Tocou'] < min:
        max = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == min:
        print(musica['Tocou'])
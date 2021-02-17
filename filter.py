"""
Filter

Filter()-> Serve para filtrar dados de uma determinada coleção.


"""
import statistics

# Dados coletados

dados = [1.3, 2.3, 3.3, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

# OBS: Assim como map(), a filter() recebedois parâmetros

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter()eles são excluídos da memória.

países = ['', 'Argentina', '', 'Brasil', '', 'Chile']

# Filtrar vazios

#res = filter(lambda país: len(país) > 0, países)
res = filter(lambda país: país != '', países)

print(list(res))


################################

# A Diferença entre map e Filter

# Map() -> Recebe dois parâmetros, uma função e um interável e retorna um objeto mapeando a função para cada elemento do intarável
# Filteer() -> Recebe dois parâmetros, uma função e um interável e retorna um objeto filtrando apenas os elementos de acordo com a função(V/F)

################################

# Exemplo mais complexos

usuarios = [
    {"username": "Samuel423", "tweets": [
        "Eu sou de esquerda", "Apoio o Psol"]},
    {"username": "Carla23", "tweets": ["Eu sou de direita", "Apoio o Psc"]},
    {"username": "Miguellll", "tweets": []},
    {"username": "Dogface", "tweets": []}

]

# Filtrar os usuários inativos

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)


################################

# Filter e map

nomes = ['Vanessa', 'Ana', 'Maria']


# DEvemos criar uma lista contendo o nome com menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(
    lambda nome: len(nome) < 5, nomes)))

print(lista)

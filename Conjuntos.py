"""
Conjuntos

Teoria dos Conjuntos

-No python os conjuntos são chamados de Sets

-Sets não possuem valores duplicados
-Sets não possuem valores ordenados
-Sets não são acessados via índice, ou seja, conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos 
com a ordenação deles. Quando não precisamos de se preocupar com chaves, valores e itens duplicados.

Diferença entre Conjuntos (set) e Mapas (Dicionários) em Python:
    -Um dicionário tem chave/valor;
    -Um conjunto tem apenas valores

"""

# Definindo um conjunto

# Forma 1

s = set({1, 1, 2, 3, 4, 24, 6, 43})  # Números repetidos são ignorados

print(s)
print(type(s))

# Forma 2 - Mais comum

s2 = {1, 1, 2, 3, 4, 24, 6, 43}

print(s2)
print(type(s2))

############

# Listas, Tuplas, >> set

#set(Listas, Tuplas)

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Importante lembrar que, além de não termos valores duplicados, não temos ordem

lista = [99, 2, 34, 23, 2, 34, 12, 1, 44, 5]
print(f'Lista: {lista}')

tupla = (99, 2, 34, 23, 2, 34, 12, 1, 44, 5)
print(f'Tupla: {tupla}')

dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario}')  # Dicionarios não aceitam chaves duplicadas

conjunto = {99, 2, 34, 23, 2, 34, 12, 1, 44, 5}
print(f'Conjunto: {conjunto}')  # Conjuntos não aceitam valores duplicados

################################

# Podemos misturar os tipos de dados em um set

s3 = {1, 'preço', True, 32.22}

print(s3)

# interar

for valores in s3:
    print(valores)


################################

# Adicionando elementos em um conjunto

cidades = ['Belo Horizonte', 'Campo Grande', 'Cuiaba', 'São Paulo']

cidades.add(4)
cidades.add(4)  # DUplicidade não gera erro

# removendo valores

# Forma 1
cidades.remove('Belo Horizonte')

# Forma 2
cidades.discard(4)

################################


# COPIANDO

# Forma 1 - DeepcoPy

novo = cidades.copy()

novo.add(5)

print(novo)
print(cidades)

# Forma 2 -> Shallow copy

novo = cidades

novo.add(5)

print(novo)
print(cidades)

############

novo.clear()

################################

# Métodos Matemáticos

estudantes_python = {'Henrique', 'Ana', 'João', 'Pedro'}

java_students = {'Fernando', 'Ana', 'Gabriela', 'Marcos'}

# União entre dois conjuntos

# Forma 1
uniao = estudantes_python.union(java_students)

print(uniao)

# Forma 2 -> |

uniao2 = java_students | (estudantes_python)


""""""""

# Intersecção

# Forma 1
ambos = estudantes_python.intersection(java_students)

print(ambos)

# Forma 2 -> &

ambos2 = java_students & estudantes_python

print(ambos2)


""""""""

# Diferença

so_python = estudantes_python.difference(java_students)

print(so_python)

so_java = java_students.difference(estudantes_python)

print(so_java)


################################

s = {1, 1, 2, 3, 4, 24, 6, 43}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

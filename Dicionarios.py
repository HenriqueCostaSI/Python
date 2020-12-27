"""
Dicionarios

Obs: Conhecidos tambem como maps

Dicionarios sao colecoes do tipo chave e valor

Representados por {chave:valor, ...,}

Podem ser de qualquer tipo de dados, inclusive mistura-los

->NAO podemos ter chaves repetidas

"""
#Forma 1 (Mais comum)
paises = {'BR':'Brasil', 'EUA':'Estados Unidos', 'UK':'United Kingdom'}

#Forma 2 

paises2 = dict(BR='Brasil', EUA='Estados Unidos', UK='United Kingdom')


""""""

#Acessando Elementos

#Forma 1 - Acessando via chave 

print(paises['BR'])
print(paises['UK'])

#forma 2 -> RECOMENDADA

print(paises.get('BR'))
print(paises.get('EUA'))
print(paises.get('USA'))#Retorna o tipo None

pais = paises.get('RU')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o pais')

""""""

#Verificando

print('br' in paises)
print('Estados Unidos' in paises)

""""""
#Usando varios tipos

localidades = {
    (34.4395, 32.65945): 'Escritorio em Tokio'
    (123.4395, 3234.65945): 'Escritorio em NY'

}

""""""""

receita = {'jan': 1230}

receita['fev'] = 3244

novoDado = {'mar': 2465}

receita.update(novoDado)

################################

#Atualizando os Dados

receita['mar'] = 5565

receita.update({'mar': 600})

""""""

#REMOVER dados de um dicionário

#Forma 1
receita.pop['mar']

#Forma 2
del receita['fev']

print(receita)

################################

#Adicionar

carrinho = {}

produto1 = {'nome': 'Playstation 4', 'quantidade':1 , 'preço': 2350}
produto2 = {'nome': 'Xbox', 'quanaitida': 2, 'preço':2300}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

################################

#Métodos de dicionário

d = dict(a=1, b=2, c=3)

print(d)

#Limpar Dicionario

d.clear()

################################

#COPIANDO

novo = d.copy()#DEEPCOPy

novo['d'] = 439

print(d)
print(novo)

#Shallow Copy

novo = d

novo['d'] = 439

print(d)
print(novo)

################################

#Forma nao usual de criação de dicionários

outro = {}.fromkeys('a','b','c')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email'], 'Desconhecido')

print(usuario)
print(type(usuario))

#O método from keys recebe dois parâmetros: um interável e um valor

veja ={}.fromkeys(range(1,11), 'novo')

print(veja)

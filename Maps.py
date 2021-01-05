<<<<<<< HEAD
"""
Maps == Dicionarios


"""

receita = {'jan': 100, 'fev': 230 , 'mar': 321}

#interar sobre dicionarios

for chave in receita:
    print(chave)


for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

#Acessando as chaves
print(receita.keys())

#Acessando os valores para
print(receita.values())

for valor in receita.values():
    print(valor)

#Modo recomendado
for chave in receita.keys():
    print(receita[chave])

#Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave={chave} e valores={valor}')

#Soma, Valor Máximo , Valor Minimo e tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values())

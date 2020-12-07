"""
Listas

Listas em Python funcional como vetores/matrizes (arrrays) em outras linguagens, com a diferença de serem DINÂMICO e tambem de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: arrays
- Possuem Tamanho fixo e tipo de dado fixo

Já em Python>

-Dinâmico: não possui tamanho  fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos
-Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado

As listas em Python são representadas com []


"""

#type([])

lista1 = list("Geek Universe")

lista2 = list(range(1, 11))

#podemos verificar se determinado valaor está contido na lista

numero = input('Digite um número para verificar se ele está na lista: ')

if numero in lista2:
    print(f'O numero {numero} está contido na lista') 
else:
    print(f'O número {numero} não foi encontrado')

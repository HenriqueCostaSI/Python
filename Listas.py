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

lista3 = [443, 543, 88, 92, 49]

#podemos verificar se determinado valaor está contido na lista

numero = input('Digite um número para verificar se ele está na lista: ')

if numero in lista2:
    print(f'O numero {numero} está contido na lista') 
else:
    print(f'O número {numero} não foi encontrado')


""""""

#Ordenando uma lista

lista3.sort()
print(lista3)

#Contador

print(lista3.count(1))
print(lista1.count('e'))

""""""

#Adicionar
#Obs:Com append, nós conseguimos adicionar um elemento por vez

print(lista3)
lista3.append(766)
print(lista1)

lista3.append([8, 3, 1])
print(lista3)

if [8, 3, 1] in lista3:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

#Coloca cada elemento da lista como valor adicional á lista 

lista3.extend([0, 29, 98])


#Podemos inserir um novo elemento na lista informando o índice
#Obs: Isso não substitui o valor inicial.

lista3.insert(2, 100)
print(lista3)

""""""

#INVERTER

lista3.reverse()
print(lista3)

print(lista1[::-1])#forma 2

""""""

#COPIAR

lista2 = lista3.copy()
print(lista2)

""""""

#Contar Elementos

print(len(lista3))


"""
#REMOÇÃO DE ELEMENTOS

"""
#REMOVER O ULTIMO ELEMENTO e o retorna

print(lista2)
lista2.pop()
print(lista2)

#Podemos remover pelo índice

lista2.pop(2)
print(lista2)


#Removendo todos os elementos

lista2.clear()

""""""

#Repetir elementos 

lista2 = [1, 2, 3]
lista2 = lista2 * 3
print(lista2)

""""""

#String -> Lista

curso = 'Programação em Python'
curso = curso.split()   #Ele separa pelos espaços entre elas
print(curso)

###

curso = 'Program,Python'
curso = curso.split(',')
print(curso)

""""""

#Lista -> String

lista6 = ['Programação', 'em', 'Python']

curso = ' '.join(lista6)
print(curso)

""""""

#Interando sobre listas

soma = 0

for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

"""
#Usando o while

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite SAIR: ')
    produto = input()
    if produto != 'sair':
       carrinho.append(produto)
    
for produto in carrinho:
    print(produto)

"""

""""""

#Utilizando variáveis

numeros = range(1, 10)
print(numeros)

num1 = 1
num2 = 29
num3 = 100

lista7 = [num1, num2, num3]

""""""

#Acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul']

print(cores[0])
print(cores[2])

#Acesso aos elementos de forma inversa

print(cores[-1])


""""""

for cor in cores:
    print(cor)

i = 0
while i < len(cores):
    print(cores[i])
    i += 1


""""""

#Gerar indice em um for

for indice, cor in enumerate(cores):
    print(cor, indice)


""""""

#Encontrar o índice de um elemento

numeros = [ 32, 242, 34, 56 , 4, 2, 89]

print(numeros.index(32))

print(numeros.index(241))

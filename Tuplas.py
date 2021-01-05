"""
Tuplas (tupla)

1-> Representadas por , e parentêses.
2-> Elas são imutáveis, toda operação com uma tupla gera um anova tupla 

tupla1= (1, 2, 3)
tupla2 = 1, 2, 3

 #Cuidado tupla de um elemento, deve ter uma virgula

 tupla11 =  (1,)
(1) -> não é tupla de

################################

tupla4 = tuple(range(12))

################################


"""

#Desempacotamento de tuplas

tupla = (1, 'Olá')

num, texto = tupla

print(texto)
print(num)

""""""

#Se os valores forem numeros

print(sum(tupla11))
print(max(tupla11))
print(min(tupla11))
print(len(tupla11))

""""""

#Concatenação de Tuplas

tupla1 = (1, 3, 4)
tupla2 = (5, 6, 7)

print(tupla1 + tupla2)
##Elas não serão alteradas

""""""
#Podemos sobrescrever seus valores

tupla1 = tupla1 + tupla2

""""""

#verificar se está contido

print(3 in tupla1)


""""""

#Interando sobre uma tupla

for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)


""""""

#Contando um elemnto da tupla

print(tupla1.cont(3))

""""""

#String -> tuple

escola = tuple("Geek Universe")

print(escola.count('e'))


# Dicas para utilização de Tuplas

##Devemos Utiliuzar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

###Exemplos meses do ano meses("Janeiro", "Fevereiro", ...)

""""""

#Acesso via indice

print(escola[1])

""""""
#interar usando While

while i < len(escola):
    print(escola[2])
    i = i + 1

""""""

#Verificamos em qual índice um elemento está na tupla1

print(meses.index('a'))

#Obs: Caso o elemento não exista, será gerado ValueError

"""""""

#Slicing
##tupla(inicio:fim:passo)

print(tupla[3:])

""""""
nova = tupla1 #Na tupla nao temos o problema de Shallow copy


#############################################################################


"""
->TUPLAS SÃO MAIS RAPIDAS
->SÃO MAIS SEGURAS
""""""

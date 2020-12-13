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

tupla1 = (1,3, 4, 5)
"""
Ranges
-Precisamos conhecer o loop for para usar os ranges.
-Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges sao utilizadas para gerar sequencias numérias, nap de forma aleatória.
"""

"""
Formas gerais:

range(valor de parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo 1 em 1)

1#

for num in range(11):
    print(num, end= ' ')

"""
"""
2#

range(valor_de_inicio, valor_de_parada)

OBS:valor_de_parada não inclusive (inicio especificado pelo usuária, e passo de 1 em 1)
"""
for num in range(1, 10):
    print(num)

"""
# Forma 3

range(valor_de_inicio, valor_de_parada, Passo)

"""
for num in range(1, 10, 2):
    print(num)

"""

# Forma 4 {Inversa}

range( valor_de_parada, valor_de_inicio, Passo)

"""

for num in range(10, 0, -1):
    print(num)
"""
Loop for

Loop -> estruturas de repeticao
For -> uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    }

python

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis:

-strings
-Lista
_Range
    numeros = range(1, 10)

"""
"""
nome = 'Geek Universe'
lista = {1, 3, 5, 7, 9}
numeros = range(1, 10)


for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in range(1, 10):#
    print(numero)

for i, v in enumerate(nome):
    print(nome[i])

"""

"""

qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

"""

qtd = int(input(f'Digite um numero: '))
num = 1

for _ in range(1, qtd + 1):
    print(f'{num}')
    num = num + 1






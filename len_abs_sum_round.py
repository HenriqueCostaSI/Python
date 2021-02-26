"""
Len, Abs, Sum e Round

#Len()

len()-> Retorna o tamanho de um interável
"""
# Exemplos
print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len({'a': 1, 'b': 2, 'c': 3}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() e o Python faz o seguinte:

# Dunder len
print('Geek University'.__len__())

################################################################

"""
abs()-> Retorna o valor absoluto
"""

# Exemplos Abs

print(abs(-5))
print(abs(-3.14))

################################################################

"""
Sum()-> Recebe como parâmetro um iteráve, podendo receber um valor inicial, e retorna a soma total dos elmentos, incluindo o valor inicial.

Obs: O valor inicial é o default = 0
"""

# Exemplos

print(sum([1, 2, 3, 323, 45]))

print(sum([1, 2, 3, 323, 45], 5.32))

print(sum(1, 2, 3, 323, 45))

print(sum({1, 2, 3, 323, 45}))

print(sum({'a': 1, 'b': 2, 'c': 3}.values()))

################################################################

"""
#Round

round() -> Retorna um número arredondado para n dígito de precisão após a casa decimal. Se a precisão não for informada 
retorna o inteiro mais próximo da entrada
"""
# Exemplos Round

print(round(10.2))

print(round(1.234234324, 2))

print(round(3.1345324, 3))

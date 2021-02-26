"""
Reversed-> Inverter o Interável


Obs: Não confunda com reverse() de listas

A função retorna um List Reverse Iterator
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto
print(set(reversed(lista)))  # Em conjunto nós não guardamos ordem inv

################################

# Podemos interar sobre o reversed
for letra in reversed("Geek University"):
    print(letra, end='')

# Podemos fazer o mesmo sem o forma
print(''.join(list(reversed("Geek University"))))

# Já Vimos como fazer isso mais fácil com o slice de strings
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)

"""
Any e All

all() -> retorna true se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

"""
# Exemplo all()

print(all([0, 1, 2, 3]))  # Todos os números são verdadeiro?False
print(all([1, 2, 3]))  # Todos os números são verdadeiro?True
print(all([]))  # Todos os números são verdadeiro?False

nomes = ['Carlos', 'Camila', 'Carla']

print(all([nome[0] == 'C' for nome in nomes]))  # True

# Obs: um interavel vazio o all entende como true
print(all([letra for letra in 'eio' if letra in 'aeiou']))

################################

print(all([num for num in [4, 2, 3, 10] if num % 2 == 0]))

"""
Any -> Retorna True se qualquer elemento do interável for verdadeiro. Se o iterável estiver vazio, retorna False


"""

print(any[0, 1, 3, 4])  # true

nomes = ['Carlos', 'Camila', 'Carla', 'Daniel']

print(any(nome[0] == 'C' for nome in nomes))

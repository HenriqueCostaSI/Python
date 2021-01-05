<<<<<<< HEAD
"""
Deque -> Podemos dizer que deque é uma lista de alta performance 

"""

# Importa

from collections import deque

# Criando deque

deq = deque('geek')

print(deq)

# Adicionando elementos no deque

deq.append('y')  # Adiciona no final

deq.appendleft('k')  # Adiciona no começo

# remover

print(deq.pop())

print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento

print(deq)

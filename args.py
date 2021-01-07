"""
Entendo o *args

-> O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, 
desde que começa com asterísco.

Exemplo: valor_de_parada

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args

O parâmetro *args utilizando em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis

"""
# Exemplo


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 7, 9))

# print(soma_todos_numeros(4, 7))# Typerror

# print(soma_todos_numeros(4, 5, 6, 7))# Typerror

###############################################################

# Entendo o Args


def soma_todos_numeros2(*args):
    return sum(args)
    """total = 0
    for numero in args:
        total = total + numero
    return total"""


print(soma_todos_numeros2())
print(soma_todos_numeros2(1))
print(soma_todos_numeros2(2, 3))
print(soma_todos_numeros2(3, 4, 5, 6, 9))

def soma_todos_numeros3(nome, *args):
    return sum(args)
    """total = 0
    for numero in args:
        total = total + numero
    return total"""


print(soma_todos_numeros2('Henrique'))
print(soma_todos_numeros2('Henrique', 1))
print(soma_todos_numeros2('Henrique', 2, 3))
print(soma_todos_numeros2('Henrique', 3, 4, 5, 6, 9))

###############################################################

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek!'
    return 'Eu nãp tenho certeza quem você é ...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(1, 'University', 3.132)

###############################################################

def soma(*args):
    return sum(args)



numeros = [1, 2, 3, 4, 5, 6] 

# print(soma(numeros)) TYPERROR
# ele sempre fará uma tupla
# logo ([1, 2, 3, 4, 5, 6], )

# print(soma(numeros, 4, 5, 6)) # TYPERROR

print(soma(*numeros))

# OBS: O asteisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# desda forma ele executará um desempacotamento

"""
Funções com parâmetro (de entrada)

"""

# Refatorando a função


def quadrado(numero):
    return numero ** 2


print(quadrado(2))

ret = quadrado(3)

print(ret)

################################

# OBS: Funções podem ter n parâmetros de entrada separados por vírgula


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(multiplica(24, 94))
print(outra(29, 348, 'Python'))

################################


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


nome = 'Henrique'
sobrenome = 'Matheus'

# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados na execução de uma função

################################

# Argumentos nomeados  (Keyword Arguments)

print(nome_completo(nome='Henrique', sobrenome='Matheus'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Matheus', nome='Henrique'))

################################

# Erro na utilização de return


def soma_ímpares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + numeros
       # return total, errado
    return total


lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(soma_ímpares(lista))

"""
Funções com Parâmetro Padrão (Default Paramters)

# Exemplo onde a passagem de parâmetro seja opcional print()


Por quê utilizar
-> Nos permite ser mais flexiveis nas funções
-> Evita erros com parâmetros incorretos
-> Nos permite trabalhar com exemplos mais legíveis de código

"""


def exponencial(numero, potencia):
    return numero * potencia


print(exponencial(9, 3))

# Refatorando


def exponencial2(numero, potencia=2):
    return numero * potencia


print(exponencial2(4))

# Se o usuário passar somente um argumento, ele será atribuido ao primeiro parâmetro


def exponencial3(numero=4, potencia=2):
    return numero * potencia


print(exponencial3())

################################

# ERRADO

# def teste(num = 2, potencia):
#    return num ** potencia


################################

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-Vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Acesso negado'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Henrique'))

################################

# Funções como parâmetro


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao)

################################

# EscopoDeVariaveis
# Variaveis globais

x=5

def teste():
    return 34

# Variaveis locais

def teste2():
    x=65945
    return x

"""
WARNING: EVITE VARIAVEIS GLOBAIS
"""

total=0

def incremento():
    global total  # Avisando que queremos utilizar a variavel global
    total=total + 1
    return total

################################

# Podemos ter funções declaradas dentro de funções

def fora():
    contador=0
    def dentro:
        nonlocal contador
        contador=contador + 1
        return contador
    return dentro()

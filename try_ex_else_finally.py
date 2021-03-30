"""
Try / Except / Else / Finally


Dica de quando tratar o código: TODA ENTRADA deve ser TRATADA!

"""
num = 0
#Else -> É executado somente se não ocorrer o erro
try:
    num = int(input("Informe um número"))
except ValueError:
    print("Valor incorreto")
else:
    print(f'Você digitou {num}')


# Finally

try:
    num = int(input("Informe um número"))
except ValueError:
    print("Valor incorreto")
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')

# O bloco Finally SEMPRE é executado
# O finally geralmente é utilizado para fechar ou desalocar recursos


# Exemplo mais complexo errado

def dividir(a, b): 
    return a / b


num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('Valor precisa ser numérico')


try:
    print(dividir(num1, num2))
except:
    print('Valor incorreto')

# Exemplo Complexo correto
# OBS: Você é responsável pelas entradas das suas funções. 

def dividir(a, b):
    try: 
        return int(a) / int(b)
    except ValueError:
        print('Valor incorreto')
    except ZeroDivisionError:
        return 'Não é possível uma divisão por zero'


num1 = input('Informe o primário número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Exemplo Complexo genérico
# OBS: Você é responsável pelas entradas das suas funções. 

def dividir(a, b):
    try: 
        return int(a) / int(b)
    except:
        return 'Ocorreu um erro'


num1 = input('Informe o primário número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Exemplo Complexo semi-genérico
# OBS: Você é responsável pelas entradas das suas funções. 

def dividir(a, b):
    try: 
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'


num1 = input('Informe o primário número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
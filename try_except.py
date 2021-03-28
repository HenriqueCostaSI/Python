"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo

try:
    //execuçao problemática
except:
    //o que deve ser feito em caso de problema para

"""

try:
    geek()
except:
    print('Deu algum problema')

# TEnte executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

try:
    len()
except:
    print('Deu algum problema')

# TEnte executar a função len(), caso você encontre erros, imprima a mensagem de erro.

##Obs: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma específica.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

# Exemplo 3 - Tratando um erro específico

try:
    geek(5)
except NameError:
    print('Você está utilizando uma função inexistente.')

# Exemplo 4 - Tratando um erro específico

try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente.')

# Exemplo 5 - Tratando um erro específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Exemplo 6 - Tratando um erro específico com detalhes do erro

try:
    len(5)
except NameError as erra:
    print(f'A aplicação gerou o seguinte erro: {erra}')
except TypeError as errb:
    print(f'Deu um TypeError: {errb}')
except:
    print('Deu um erro diferente')

# Exemplo

def pega_valor(dicionario, chaves):
    try:
        return dicionario[chaves]
    except KeyError:
        return None
    except TypeError:
        return None
        
dic = {"nome": "Geek"}

print(pega_valor(dic, "nome"))
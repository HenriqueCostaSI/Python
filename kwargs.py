"""
Este é só mais uma parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwarg exige que utilizemos 
parâmetros nomeados, e transdorma esses parâmetrosextras em um DICINÁrio.

"""

# EXEMPLO


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')
    print(kwargs)


cores_favoritas(marcos='Vermelho', julia='Verde',
                fernando='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwarg não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')

# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='OI'))
print(cumprimento_especial(geek='especial'))

################################################################

# Nas nossas funções podemos ter(NESTA ORDEM):
# -> parâmetros obrigatóros
# -> *args
# -> Parâmetros default
# -> **kwargs


def minha_funcao(idade, nome,  *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Ana', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 7, 8, java=False, python=True)

# Exemplo por quê é importante manter a ordem dos parãmetros na declaração


# Função com a ordem correta de parãmetros
def mostra_info(a, b, 8args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

###############################################################

# Desempacotamentocom **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Fernanda', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

# Os nomes da chave em um dicionário devem ser os mesmos dos parãmetros da função

"""
Debugando com PDB

PDB -> Python Debugger

Comandos básicos do pdb
- l (listar onde estamos)
- n (próxima linha)
- p (imprime variável)
- c (continua a execução)

# A partir do python 3.7 não precisa utilizar o pdb

"""


def dividir(a, b):
    import pdb;pdb.set_trace()
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'


print(dividir(4, 7))


def dividir(a, b):
    breakpoint() ######
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'


print(dividir(4, 7))

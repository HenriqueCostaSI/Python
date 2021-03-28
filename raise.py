"""
Levantando os próprios erros com raise

raise -> lança as nossas próprias exceções e mensagens de erros 

A forma geral de utilização é:

raise TipoDoError('Mensagem de erro')

OBS: O raise, assim como o return,  finaliza a função

"""

# Exemplo


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto must be a string')
    if type(cor) is not str:
        raise TypeError('cor must be a string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 4)

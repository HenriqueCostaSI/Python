"""
Documento funções com Docstring

"""

# Exemplosc

def diz_oi():
    """Uma função simples que retorna a string 'oi'"""
    return 'Oi!'

print(diz_oi.__doc__)

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' à 'pontencia'
    :param numero: Número que desejamos gerar o exponencial 
    :param potencia: Potência que queremos gerar o exponencial
    :return: Retorna o exponencial de 'numero' por 'potencial'
    """
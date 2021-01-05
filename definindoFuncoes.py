<<<<<<< HEAD
"""
Definindo Funções 

- Funções são pequenos partes de código que realizam tarefas específicas;
- Podem ou não receber entradas de dados e retomar uma saída de dados; 


"""

# DRY - Dont Reapeat Yourself  - Não repita seu código de

"""
Em Python, a forma geral de definir uma função é:

def nome_da_função(parâmetros_de_entrada):
    bloco_de_função


Onde:

nome_da_função -> SEMPRE com letras minúsculas, e se for nome composto, separado por underline (Snake Case):
parâmetros_de_entrada -> Opcionais, onde tendo mais de um, cadaum separado por vírgula, podendo ser opcionais ou não.
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter o não retorno da função

OBS: Veja que para definir uma função , utilizamos a palavra DEF informando ao python que estamos definindo uma função.
Também abrimos o bloco de código com o já conhecido dois pontos: que é utilizado em python para definir blocos.

"""

# Definindo a primeira função


def diz_oi():
    print('oi')


"""
OBS: 

1- Veja que, dentro das nossas funções podemos utilizar outras funções:
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi:
3 - Veja que esta função não recebe nenhum parâmetro de entrada:
4 - Veja que esta função não retorna nada:

"""

# Chamada de execução

diz_oi()  # NÃo esqueça dos parênteses


# Exemplo 2

def menu():
    print('Digite 1 para sair')


for n in range(5)
menu()

# Em Python, podemos inclusive criar variaveis do tipo de uma funçãoe executar esta função através da variável de

menu1 = menu()

menu()

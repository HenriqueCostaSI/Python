"""
https://docs.python.org/3/library/collections.html

Default Dict -> Ao criar um dicionário utilizando-o , nós informamos um valoer default, podendo utilizar um lambda para isso.
Este valor será utilizado sempre que não houver um valor definido, caso tentemos acessar uma chave que não existe, 
essa chave será criada eo valor default será atribuido


"""
"""
dict = {'cursor':'Programacao em Python'}

print(dict)

print(dict['cursor'])

print(dict['outro'])#Key error

OBS:Lambdas são funções sem nome, que podem ou nçao receber parâmetros e retornar valores

"""
#Fazendo imports

from collections import defaultdict 


dict = defaultdict(lambda: 0)

dict = {'cursor':'Programacao em Python'}

print(dict)

print(dict['outro'])
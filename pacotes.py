"""
Pacotes

Pacotes -> É um diretório contendo uma coleção de Módulos

Módulos -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos

OBS:O arquivo _init_.py é para manter compatibilidade com as versões 2.x do Python

"""

from geek import geek1, geek2

print(geek1.pi)

print(geek1.funcao(4, 6))

print(geek2.curso)

print(geek2.funcao2)

from geek.geek0 import geek3

print(geek3.pap)

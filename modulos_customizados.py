"""
Módulos Customizados


Como módulos Python nada mais são que arquivos Python, Logo TODOS os meus arquivos são módulos Python
"""

from  funçoes_com_parametro import soma_ímpares

print(soma_ímpares([1, 2, 3, 4, 5]))

############################################################

#Importando TODO o módulo

import funçoes_com_parametro as fcp 

# Estamos acessando e imprimindo uma variável contida no módulo
print(fcp.lista)

print(fcp.soma_impares(fcp.lista))

######################################################

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))

"""
Módulo Random e o que são módulos?

- Em Python, módulos são outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.


"""

# OBS: Existem duas formas de se utilizar um módulo ou função desempacotamento

# Forma 1 - Importando todo o módulo (Não recomendado).

from random import choice
import random import radiant
from random import uniform
from random import random
import random

# random()-> Gera um número pseudo-aleatório entre 0 e 1.

# OBS: Ao realizar o import de todo módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo dicarão disponíveis (Ficarão em Memória). Caso você saiba quais funções você precisa utilizar
# desde módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função, separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random é
# apenas uma função dentro do módulo random.

########################################################################################################################################

# Forma 2 - Importando uma função específica do módulo


# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

########################################################################################################################################

# uniform() -> Gerar um número real pseudo-aleatório entra os valores estabelecidos


for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído

########################################################################################################################################

# radiant() -> Gera valores inteiros pseudo-aleatório

# Gerador de apostas para mega_sena

for i in range(6):
    print(radiant(1, 61), end=', ')  # começa em 1 e vai até 60

########################################################################################################################################

# choice() -> Mostra um valor aleatório entre um iterável


jogadas = ['pedra', 'papel', 'tesoura']


print(choice(jogadas))

########################################################################################################################################

# shuffle() -> Tem a função de embaralhar Dados

cartas = ['k', 'q', 'j', 'a', '2', '3', '4', '5', '6', '7']

print(shuffle(cartas))

print(cartas.pop())

"""
Módulos Externos 

Utilizamos o gerenciador de pacotes Python chamado Pip

https://pypi.org/project/pip/

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

from colorama import init, Fore

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')

"""

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><strongPrograma&ccedil;&atilde;o em Python: Essencial</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

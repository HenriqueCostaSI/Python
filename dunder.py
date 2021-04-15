"""
Dunder name e Dunder Maintenance

Dunder -> Doble Under 

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando Double Under para não gerar conflito com os 
nomes desses elemenros na programação

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal

#Se queremos transformar um arquivo em módulo precisamos nos preocupar com isso e com os prints

# if __name__ == '__main__':
    print()
    .
    .
    .

#Se ele for importado ele se chamará pelo nome do arquivo

"""

from funçoes_com_parametro import soma_impares as im

if __name__ == '__main__':
    print(im([1, 2, 3]))
else:
    print("Esse Arquivo foi importado")

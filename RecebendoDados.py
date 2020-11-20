"""
Reccebendo Dados do usuário

Todo dado recebido via input são uma string, usar o CASTING


"""

#Entrada de Dados
print("Qual é seu nome:")
nome = input()

#idade = input('Qual é o seu nome')
#CASTING
#idade = int(input('Qual é o seu nome'))

#Processamento
#Exemplo de print antigo

print("Seja Bem Vindo(a) %s" % nome)

print("Qual é a sua idade:")
idade = input()

print("O %s tem %s anos" % (nome, idade))



#Exemplo de print novo


print(f'Seja Bem Vindo(a) {nome}')



print(f'O {nome} tem {idade}')

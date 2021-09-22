#1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três
# argumentos.       OK
#def soma (a, b, c):
#    soma1= a + b + c
#    return soma1

#num1= float(input('Inseira o primeiro número:'))
#num2= float(input('Inseira o segundo número:'))
#num3= float(input('Inseira o terceiro número:'))
#print('A soma de {} + {} +{}: {}.'.format(num1, num2, num3, soma(num1, num2, num3)))

#2. Uma função que necessita de um argumento. A função retorma o valor de caractere "P", se seu argumento for
#positivo, e "N", se seu argumento zero ou negativo.     OK
#def numero (a):
#    numero1 = a
#    return numero1

#num1 = float(input('Insira um número:'))
#if num1 > 0:
#        print('{} é POSITIVO!'.format(num1, numero(num1)))
#else:
#    num1 <= 0
#    print('{} é NEGATIVO!'.format(num1, numero(num1)))

#3. Uma função chamada somaImposto. Possui dois parãmetros formais: "taxaImposto", a quantidade de imposto
#sobre venda expressa em porcentagem e "custo", o custo de um item antes do imposto. A função 'altera'
# o valor de custo para incluir o imposto sobre vendas.       NÃO SEI SE ESTÁ CERTO.

#def somaImposto (a, b):
#    somaImposto1 = a*(b/100) + custo
#    return somaImposto1

#taxaImposto = float(input('Valor do imposto:'))
#custo = float(input('Valor do item:'))
#print('O valor de {} e {} é:{}.'.format(taxaImposto, custo,somaImposto(taxaImposto, custo)))

#4. Faça uma função que retorne o reverso de um número inteiro informado. Ex.: 127->721.
# NÃO SEI SE ESTÁ CERTO.

#def numero (a):
#    numero1 = 1/a
#    return numero1

#num1 = float(input('Insira um número:'))
#print('O inverso do número {} é {}.'.format(num1, numero(num1)))

#5. Faça uma função que retorne a quantidade de dígitos de um determinado número inteiro informado.
# NÃO CONSEGUI FAZER.
#class Pessoa:
#    def __init__(self, nome='', sexo='', idade=0, ativo=False):
#        self.nome = nome
#        self.sexo = sexo
#        self.idade = idade
#        self.ativo = ativo
#    def __str__(self):
#        return self.nome
#    def ativarPessoa(self):
#        self.ativo= True
#    def desativarPessoa(self):
#        self.ativo= False
#    def verificarIdade(self):
#        if (int(self.idade)>= 18):
#            print('Você é maior de idade!')
#        else:
#            print('Você é menor de idade!')

#pessoa1 = Pessoa('Maria', 'Feminino')

#print('Seu nome é:', pessoa1.nome)
#print('O sexo de {} é {}'.format(pessoa1.nome, pessoa1.sexo))
#print('Sua idade é:', )

#Dicionario de dados
meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}
#print(type(meu_dicionario))


meu_dicionario_2 = dict({1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'})
#print(type(meu_dicionario_2))

#get() Elementos pelo indice
print(meu_dicionario[2])
print(meu_dicionario.get(4))
''''
#len() Tamanho do dicionario
print(len(meu_dicionario))

#adicionando elementos no dicionario
meu_dicionario[5] = 'Joaquina'
print(meu_dicionario)

meu_dicionario.update({6: 'Pedro'})
print(meu_dicionario)

#removendo elementos do dicionario
#pop()
meu_dicionario.pop(2)
del meu_dicionario[1]
print(meu_dicionario)
'''
#visualizando dados
for id, nome in meu_dicionario.items():
    print(str(id) +": "+str(nome))
'''''
elif num1 == 3:
unicoCliente =
print('O status foi{}'.format(unicoCliente.getativo()))
unicoCliente.getdesativarCliente(int(input))

elif num1 == 3:
print(lista_cliente)
cliente = Cliente('1', 'Maria', '1234', 'rua de cima', 'queimada', 'Ribeirão', '1234-5678', 'meu@gmail.com', True)
cliente.desativarCliente()
cliente.ativo = True
print(cliente.ativo)
#
def inserir(self, id, nome, rg):
    self.nome.update({id: nome})
    self.rg.update({id: rg})

def lista_cliente(self):
    for id, nome, rg in self._nome.iteams():
        print('ID:', id)
    print('Nome:', nome)
    print('RG:', self.rg.get(id))
'''''


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

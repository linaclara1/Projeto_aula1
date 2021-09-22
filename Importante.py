'''''''''
class Cliente:
    #Construtor
    def __init__(self, id='', nome='',rg='', endereco='', bairro='', cidade='', telefone='', email='', ativo=True):
        self._id= id
        self._nome= nome
        self._rg= rg
        self._endereco= endereco
        self._bairro= bairro
        self._cidade= cidade
        self._telefone= telefone
        self._email= email
        self._ativo= ativo

    #Encapsulamento de dados
    def getId(self):
        return self._id
    def setId(self, valor):
        self._id = valor

    def getnome(self):
        return self._nome
    def setnome(self, valor):
        self._nome= valor

    def getRG(self):
        return self._rg
    def setRG(self, valor):
        self._rg = valor

    def getendereco(self):
        return self._endereco
    def setendereco(self, valor):
        self._endereco= valor

    def getbairro(self):
        return self._bairro
    def setbairro(self, valor):
        self._bairro= valor

    def getcidade(self):
        return self._cidade
    def setcidade(self, valor):
        self._cidade= valor

    def gettelefone(self):
        return self._telefone
    def settelefone(self, valor):
        self._telefone= valor

    def getemail(self):
        return self._email
    def setemail(self, valor):
        self._email = valor

    def getativar(self):
        return self._ativo
    def setativar(self):
        self._ativo = True
        print('O cliente foi ativiado com sucesso!')

    def getdesativar(self):
        return self._ativo
    def setdesativar(self):
        self._ativo = False
        print('O cliente foi desativado com sucesso!')

#Menu de opções
listas = []
lista_cliente= {1: 'Maria', 2: 'William', 3: 'Antonio'}
print('Clientes atuais=', lista_cliente)
print('------------------------------')
print('Seja bem vindo ao menu de opções!')
print('1. Para incluir.')
print('2. Para excluir.')
print('3. Para desativar.')
print('4. Para lista e dados dos clientes.')
print('------------------------------')


escolha= input('Digite "EXIT" para sair.')

while escolha != 'EXIT':
    num1 = int(input('Escolha uma das opções:'))
    print('-----------------------------------')

    if num1 == 1:

        novo_id = input('Digite o ID:')
        novo_nome = str(input('Digite o nome do cliente:'))
        novo_rg = str(input('Digite o RG:'))
        novo_endereco = str(input('Digite seu endereço:'))
        novo_bairro = str(input('Digite o bairro:'))
        novo_cidade = str(input('Digite a cidade:'))
        novo_telefone = str(input('Digite o telefone:'))
        novo_email = str(input('Digite o e-mail:'))
        novo_ativo = input('Seu status:')
        print('----------------------------------------')
        print('ID:', novo_id)
        print('Nome:', novo_nome)
        print('RG:', novo_rg)
        print('Endereço:', novo_endereco)
        print('Bairro:', novo_bairro)
        print('Cidade:', novo_cidade)
        print('Telefone:', novo_telefone)
        print('E-mail:', novo_email)
        print('Status:', novo_ativo)
        print('-----------------------------------')

    elif num1 == 2:
        print(lista_cliente)
        lista_cliente.pop(int(input('Digite um número que deseja excluir:')))
        del lista_cliente[int(input('Digite outro número que deseja excluir:'))]
        print(lista_cliente)
        print('-----------------------------------')


    elif num1 == 3:
        cliente1 = Cliente('1', 'Maria', '1234', 'Rua de Cima', 'Queimada', 'Ribeirão', '1234-5678','mar@gmail.com', True)
        cliente1.setdesativar()
        cliente1.ativo = False
        print(cliente1.ativo)

    elif num1 == 4:
        for id, nome in lista_cliente.items():
            # Instanciando objetos
            cliente1 = Cliente('1', 'Maria', '1234', 'Rua de Cima', 'Queimada', 'Ribeirão', '1234-5678',
                               'mar@gmail.com', True)
            cliente2 = Cliente('2', 'William', '4567', 'Rua Florida', 'Limoeiro', 'São Tome', '4567-5678',
                               'wil@gmail.com', True)
            cliente3 = Cliente('3', 'Antonio', '8901', 'Rua Bonita', 'Cocorico', 'Boa Vista', '8901-2345',
                               'ant@gmail.com', True)
            print('ID:', cliente1.getId())
            print('Nome:', cliente1.getnome())
            print('RG:', cliente1.getRG())
            print('Endereço:', cliente1.getendereco())
            print('Bairro:', cliente1.getbairro())
            print('Cidade:', cliente1.getcidade())
            print('Telefone:', cliente1.gettelefone())
            print('E-mail:', cliente1.getemail())
            print('Status:', cliente1.getativar())
            print('------------------------------------')
            print('ID:', cliente2.getId())
            print('Nome:', cliente2.getnome())
            print('RG:', cliente2.getRG())
            print('Endereço:', cliente2.getendereco())
            print('Bairro:', cliente2.getbairro())
            print('Cidade:', cliente2.getcidade())
            print('Telefone:', cliente2.gettelefone())
            print('E-mail:', cliente2.getemail())
            print('Status:', cliente2.getativar())
            print('-----------------------------------')
            print('ID:', cliente3.getId())
            print('Nome:', cliente3.getnome())
            print('RG:', cliente3.getRG())
            print('Endereço:', cliente3.getendereco())
            print('Bairro:', cliente3.getbairro())
            print('Cidade:', cliente3.getcidade())
            print('Telefone:', cliente3.gettelefone())
            print('E-mail:', cliente3.getemail())
            print('Status:', cliente3.getativar())
            print('-----------------------------------')
            print(str(id) + ": " + str(nome))

    else:
        print('Tenti outra opção!')




#Menu de opções
lista_clientes= {1:'Maria', 2:'Willian', 3:'Antonio'}
print('Clientes atuais=', lista_clientes)

print('Menu de opções')
print('1. Para incluir.')
print('2. Para excluir.')
print('3. Para acessar status.')
print('4. Para listar os clientes.')
print('5. Para ver status.')


escolha= input('Digite "EXIT" para sair.')
while escolha != 'EXIT':
    num1= int(input('Escolha uma das opções:'))
    if num1 == 1:
        novo_nome = input('Digite o nome do cliente:')
        novo_RG= float(input('Digite o RG:'))
        novo_endereço= input('Digite seu endereço:')
        novo_bairro= input('Digite o bairro:')
        novo_cidade= input('Digite a cidade:')
        novo_telefone= float(input('Digite o telefone:'))
        novo_email= input('Digite o email:')
        novo_ativo= input('Seu status:')
        print(lista_clientes)
        lista_clientes.update({4: novo_nome})
        print(lista_clientes)
    elif num1 == 2:
        excluir= input('aperte "a" para mostrar a lista')
        print(lista_clientes)
        lista_clientes.pop(int(input('Digite um número que deseja excluir:')))
        del lista_clientes[int(input('Digite outro número que deseja excluir:'))]
        print(lista_clientes)
    elif num1 == 3:
'''''''''''









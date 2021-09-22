from UC import criar_conexao, fechar_conexao

# ==================INSERIR=================
def inserir_endereco(con, cod_endereco, cep, complemento, bairro, numero, cidade):
    cursor = con.cursor()
    sql = "INSERT INTO endereco(cod_endereco, cep, complemento, bairro, numero, cidade) values (%s, %s, %s, %s, %s, %s);"
    valores = (cod_endereco, cep, complemento, bairro, numero, cidade)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


def inserir_editora(con, cod_editora, nome_gerente, cod_endereco, telefone):
    cursor = con.cursor()
    sql = "INSERT INTO editora(cod_editora, nome_gerente, cod_endereco, telefone) values(%s, %s, %s, %s);"
    valores = (cod_editora, nome_gerente, cod_endereco, telefone)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


def inserir_cliente(con, cod_unico, nome, cod_endereco, tipo_cliente, cnpj_cpf, telefone):
    cursor = con.cursor()
    sql = "INSERT INTO cliente(cod_unico, nome, cod_endereco, tipo_cliente, CNPJ_CPF, telefone) values(%s, %s, %s, %s, %s, %s);"
    valores = (cod_unico, nome, cod_endereco, tipo_cliente, cnpj_cpf, telefone)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


def inserir_livro(con, isbn, autor, assunto, qtd_estoque, cod_editora):
    cursor = con.cursor()
    sql = "INSERT INTO livro(isbn, autor, assunto, qtd_estoque, cod_editora) values(%s, %s, %s, %s, %s);"
    valores = (isbn, autor, assunto, qtd_estoque, cod_editora)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


def inserir_compra(con, cod_unico, isbn, data_compra):
    cursor = con.cursor()
    sql = "INSERT INTO livro(cod_unico, isbn, data_compra) values(%s, %s, %s);"
    valores = (cod_unico, isbn, data_compra)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


# ================== DELETAR======================
def deletar_endereco(con, cod_endereco):
    cursor = con.cursor()
    sql = "Delete from endereco where cod_endereco = {}".format(cod_endereco)
    cursor.execute(sql)
    cursor.close()
    con.commit()


def deletar_editora(con, cod_editora):
    cursor = con.cursor()
    sql = "Delete from editora where cod_editora = {}".format(cod_editora)
    cursor.execute(sql)
    cursor.close()
    con.commit()


def deletar_cliente(con, cod_unico):
    cursor = con.cursor()
    sql = "Delete from cliente where cod_unico = {}".format(cod_unico)
    cursor.execute(sql)
    cursor.close()
    con.commit()


def deletar_livro(con, isbn):
    cursor = con.cursor()
    sql = "Delete from livro where isbn = {}".format(isbn)
    cursor.execute(sql)
    cursor.close()
    con.commit()


def deletar_compra(con, cod_unico):
    cursor = con.cursor()
    sql = "Delete from compra where cod_unico = {}".format(cod_unico)
    cursor.execute(sql)
    cursor.close()
    con.commit()


# =================LISTAR==================
def listar_endereco(con):
    cursor = con.cursor()
    sql = "Select * from endereco"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    print(valores_lidos)
    for linha in valores_lidos:
        print('-----------------------------------')
        print("Cod_endereco: ", linha[0])
        print("CEP: ", linha[1])
        print('Complemento:', linha[2])
        print('Bairro:', linha[3])
        print('Número:', linha[4])
        print('Cidade:', linha[5])
        print('-----------------------------------')
    cursor.close()


def listar_editora(con):
    cursor = con.cursor()
    sql = "Select * from editora"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    print(valores_lidos)
    for linha in valores_lidos:
        print('-----------------------------------')
        print("Código da editora: ", linha[0])
        print("Nome do gerente: ", linha[1])
        print('Código do endereço:', linha[2])
        print('Telefone:', linha[3])
        print('-----------------------------------')
    cursor.close()


def listar_cliente(con):
    cursor = con.cursor()
    sql = "Select * from cliente"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    print(valores_lidos)
    for linha in valores_lidos:
        print('-----------------------------------')
        print("Código do cliente: ", linha[0])
        print("Nome: ", linha[1])
        print('Código do endereço:', linha[2])
        print('Tipo do cliente:', linha[3])
        print('CNPJ_CPF:', linha[4])
        print('Telefone:', linha[5])
        print('-----------------------------------')
    cursor.close()


def listar_livro(con):
    cursor = con.cursor()
    sql = "Select * from livro"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    print(valores_lidos)
    for linha in valores_lidos:
        print('-----------------------------------')
        print("ISBN: ", linha[0])
        print("Autor: ", linha[1])
        print('Assunto:', linha[2])
        print('Qtd. no estoque:', linha[3])
        print('Código da editora:', linha[4])
        print('-----------------------------------')
    cursor.close()


def listar_compra(con):
    cursor = con.cursor()
    sql = "Select * from compra"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    print(valores_lidos)
    for linha in valores_lidos:
        print('-----------------------------------')
        print("Código do cliente: ", linha[0])
        print("ISBN: ", linha[1])
        print('Data da compra:', linha[2])
        print('-----------------------------------')
    cursor.close()


# =====================Processamento==================

def main():
    con = criar_conexao("127.0.0.1", "root", "", "livraria2")

    print('Menu de Opções')
    print('1. Endereço')
    print('2. Editora')
    print('3. Cliente')
    print('4. Livro')
    print('5. Compra')
    print('6. Sair')
    print('--------------------------')
    num1 = int(input('Escolha um número:'))
    print('--------------------------')
    # ===============Tabela Endereço=============
    while num1 != 6:
        if num1 == 1:
            opcao1 = int(input('[1] para inserir\n[2] para deletar\n[3]para ver a lista: '))
            print('--------------------------------------------------------')
            if opcao1 == 1:
                cod_endereco = input('Digite o código do endereço:')
                cep = input('Digite o cep:')
                complemento = input('Digite o complemento:')
                bairro = input('Digite o nome do bairro:')
                numero = input('Digite o número da casa:')
                cidade = input('Digite o nome da cidade:')
                print('--------------------------')
                inserir_endereco(con, cod_endereco, cep, complemento, bairro, numero, cidade)
                listar_endereco(con)
                fechar_conexao(con)

            elif opcao1 == 2:
                cod_endereco = input('Digite o código do endereço:')
                deletar_endereco(con, cod_endereco)
                listar_endereco(con)
                fechar_conexao(con)

            else:
                listar_endereco(con)

        # =============Tabela Editora=============
        elif num1 == 2:
            opcao2 = int(input('[1] para inserir\n[2] para deletar\n[3]para ver a lista: '))
            if opcao2 == 1:
                cod_editora = input('Digite o código da editora: ')
                nome_gerente = input('Digite o nome do gerente: ')
                cod_endereco = input('Digite o código de endereço:')
                telefone = input('Digite um telefone: ')
                inserir_editora(cod_editora, nome_gerente, cod_endereco, telefone)
                listar_editora(con)
                fechar_conexao(con)

            elif opcao2 == 2:
                cod_editora = input('Digite o código da editora:')
                deletar_editora(con, cod_editora)
                listar_editora(con)
                fechar_conexao(con)

            else:
                listar_editora(con)

        # =============Tabela Cliente=============
        elif num1 == 3:
            opcao3 = int(input('[1] para inserir\n[2] para deletar\n[3]para ver a lista: '))
            if opcao3 == 1:
                cod_unico = input('Digite código unico:')
                nome = input('Digite o nome:')
                cod_endereco = input('Digite código do endereço:')
                tipo_cliente = input('Jurídico ou físico:')
                cnpj_cpf = input('Digite o CNPJ ou o CPF:')
                telefone = input('Digite o telefone:')
                inserir_cliente(con, cod_unico, nome, cod_endereco, tipo_cliente, cnpj_cpf, telefone)
                listar_cliente(con)
                fechar_conexao(con)

            elif opcao3 == 2:
                cod_unico = input('Digite o código unico:')
                deletar_cliente(con, cod_unico)
                listar_cliente(con)
                fechar_conexao(con)

            else:
                listar_cliente(con)

        # ===============Tabela Livro===========
        elif num1 == 4:
            opcao4 = int(input('[1] para inserir\n[2] para deletar\n[3]para ver a lista: '))
            if opcao4 == 1:
                isbn = input('Digite o ISBN: ')
                autor = input('Digite o nome do autor:')
                assunto = input('Digite qual o assunto:')
                qtd_estoque = input('Digite qual a quantidade:')
                cod_editora = input('Digite o código da editora:')
                inserir_livro(con, isbn, autor, assunto, qtd_estoque, cod_editora)
                listar_livro(con)
                fechar_conexao(con)

            elif opcao4 == 2:
                isbn = input('Digite o ISBN:')
                deletar_livro(con, isbn)
                listar_livro(con)
                fechar_conexao(con)

            else:
                listar_livro(con)

        # ===============Tabela Compra==============
        elif num1 == 5:
            opcao5 = int(input('[1] para inserir\n[2] para deletar\n[3]para ver a lista: '))
            if opcao5 == 1:
                cod_unico = input('Digite o código do cliente:')
                isbn = input('Digite o ISBN')
                data_compra = input('Digite a data da compra:')
                inserir_livro(con, cod_unico, isbn, data_compra)
                listar_compra(con)
                fechar_conexao(con)

            elif opcao5 == 2:
                cod_unico = input('Digite o código do cliente:')
                deletar_compra(con, cod_unico)
                listar_compra(con)
                fechar_conexao(con)

            else:
                listar_compra(con)

        print('Menu de Opções')
        print('1. Endereço')
        print('2. Editora')
        print('3. Cliente')
        print('4. Livro')
        print('5. Compra')
        print('6. Sair')
        print('--------------------------')
        num1 = int(input('Escolha um número:'))
        print('--------------------------')
    fechar_conexao(con)


main()

import mysql.connector


def criar_conexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)


def fechar_conexao(con):
    return con.close()
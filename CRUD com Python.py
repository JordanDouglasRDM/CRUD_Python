import mysql.connector

conexao = mysql.connector.connect(#conexão com database
    host ='localhost',
    user ='root',
    password ='',
    database ='bdyoutube',
)
cursor = conexao.cursor() #executar os comandos da minha conexão, iniciar e fechar


#estrutura de funções

def criar():
    nomeProduto = input('Informe o nome do Produto: ')
    valor = int(input('Informe o preço do produto (inteiro): '))
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nomeProduto}", "{valor}")' #observar a ordem de inserção no database (nome das colunas)
    cursor.execute(comando)
    conexao.commit()#edita o banco de dados
    print('\tCadastrado com sucesso!')
    return
def ler():
    pass
def atualizar():
    pass
def deletar():
    pass
def menu():
    print('\nEscolha uma opção: \n1.CREATE\n2.READ\n3.UPDATE\n4.DELETE\n0.Sair\n')
def main():
    print('CRUD com Python\n')
    validacao = True
    while validacao:
        menu()
        opcao = int(input('Selecione a opção desejada: '))
        if opcao == 0:
            print('\tVocê escolheu sair...')
            validacao = False

        elif opcao == 1:
            criar()
        
        
main()



# #CREATE
# nome_produto = "banana"
# valor = 7
# comando = f'INSERT INTO vendas (nome_produto, valor) ' \
#           f'VALUES ("{nome_produto}", "{valor}")' #observar a ordem de inserção no database (nome das colunas)
# cursor.execute(comando)
# conexao.commit()#edita o banco de dados
# resultado = cursor.fetchall() #ler banco de dados


# #READ
# comando = 'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

# #UPDATE
# valor = 5
# qualID = 2
# comando = f'UPDATE vendas SET valor = "{valor}" WHERE idVendas = {qualID}'
# cursor.execute(comando)
# conexao.commit()

# #DELETE
# qualID = 3
# comando = f'DELETE FROM vendas WHERE idVendas = {qualID}'
# cursor.execute(comando)
# conexao.commit()


# cursor.close()#fechar
# conexao.close()#fechar
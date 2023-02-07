import mysql.connector

class Objeto:
    id = 0
    nome = ''
    valor = 0

conexao = mysql.connector.connect(#conexão com database
    host ='localhost',
    user ='root',
    password ='',
    database ='bdyoutube',
)
cursor = conexao.cursor() #executar os comandos da minha conexão, iniciar e fechar


#estrutura de funções

def criar():#confirmar antes de enviar para o banco de dados
    nomeProduto = input('Informe o nome do Produto: ')
    valor = int(input('Informe o preço do produto (inteiro): '))
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nomeProduto}", "{valor}")' #observar a ordem de inserção no database (nome das colunas)
    cursor.execute(comando)
    conexao.commit()#edita o banco de dados
    print('\tCadastrado com sucesso!')
    return
def convertTuplaToVet(tupla):
    vetor = []
    for i in range(len(tupla)):
        obj = Objeto()
        obj.id, obj.nome, obj.valor = tupla[i][0], tupla[i][1], tupla[i][2]
        vetor.append(obj)
    return vetor
def ler():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print('\n\tID\tNOME PRODUTO\tVALOR')
    vetor = convertTuplaToVet(resultado)
    for i in range(len(vetor)):
        print(f'\t{vetor[i].id:<10}{vetor[i].nome:<15}R${vetor[i].valor}')  
def atualizar():
    qualID = int(input('Qual o Item que deseja alterar? (Insira o ID): '))
    opcao = input('Deseja altera o nome ou o valor? (n/v) ')
    if opcao in 'nN':
        opcao = 'nome_produto'
        altera = input('Informe o novo nome do produto: ')
    elif opcao in 'vV':
        opcao = 'valor'
        altera = input('Qual o novo preço do produto? ')
    comando = f'UPDATE vendas SET {opcao} = "{altera}" WHERE idVendas = {qualID}'
    cursor.execute(comando)
    conexao.commit()
def deletar():
    qualID = int(input('Qual o Item que deseja DELETAR? (Insira o ID): '))
    print(f'Você escolheu alterar o item do ID {qualID}')
    opcao = input('Deseja continuar? (s/n): ')
    if opcao in 'sS':
        comando = f'DELETE FROM vendas WHERE idVendas = {qualID}'
        cursor.execute(comando)
        conexao.commit()
        print('\tItem exluído!')
        pass
    elif opcao in 'nN':
        print('\tVocê escolheu cancelar...')
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
        elif opcao == 2:
            ler()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
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
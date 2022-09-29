#1 - cadastrar produto
#2 - consultar produto(s)
    #1 - consultar todos os produtos
    #2 - consultar produto por código
    #3 - consultar produto(s) por fabricante
    #4- Voltar
#3 - remover produto
#4 - sair

listaProdutos = []
def cadastrarProduto(codigo): #função para cadastrar produtos e gerar o codigo
    print('Cadastro de Produtos')
    print('O codigo do produto é: {}'.format(codigo))
    nome = input('Digite o nome do produto: ')
    fabricante = input('Digite o fabricante do produto: ')
    valor = float(input('Digite o valor do produto: R$'))
    dicionarioProduto = {'codigo': codigo,
                         'nome' : nome,
                         'fabricante' : fabricante,
                         'valor' : valor}
    listaProdutos.append(dicionarioProduto.copy())
def consultarProduto(): #função para consultar produtos
    while True:
        try:
            print('Consulta de produtos')
            opconsultar = int(input('Escolha a opção desejada\n'
                                    '1 - Consultar todos os produtos\n'
                                    '2 - Consultar por codigo\n'
                                    '3 - Consultar por fabricante\n'
                                    '4 - Retornar\n'
                                    '>>> '))
            if opconsultar == 1:
                print('Consultar todos os itens')
                for produto in listaProdutos: #selecionar cada dicionario da lista
                    for key, value in produto.items(): #selecionar cada conjunto chave valor do dicionario('nome' : ovo)
                        print('{} : {}'.format(key, value))
            elif opconsultar == 2:
                print('Consulta por codigo')
                entrada = int(input('Digite o codigo do produto: '))
                for produto in listaProdutos:
                    if(produto['codigo'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))

            elif opconsultar == 3:
                print('Consulta por fabricante')
                entrada = input('Digite o codigo do produto: ')
                for produto in listaProdutos:
                    if (produto['fabricante'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif opconsultar == 4:
                return
            else:
                print('Pare de digitar valores que não estão no menu')
        except ValueError:
            print('Pare de digitar valores não inteiros')
def removerProduto(): #função para remover produto
    print('Remover produto')
    entrada = int(input('Digite o codigo do produto que deseja remover: '))
    for produto in listaProdutos:
        if (produto['codigo'] == entrada):
           listaProdutos.remove(produto)
# ---------- Programa Principal ----------
print('Cadastro de produtos Wilson Gabriel de Souza')
codigo = 0
while True:
    try:
        opcao = int(input('Digite a opção desejada:\n'
                          '1 - Cadastrar produto\n'
                          '2 - Consultar produto\n'
                          '3 - Remover produto\n'
                          '4 - Sair\n'
                          '>>> '))
        if opcao == 1:
            codigo += 1
            cadastrarProduto(codigo)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Programa encerrado')
            break
        else:
            print('Pare de digitar números que não existem no menu')
            continue
    except ValueError:
        print('Pare de digitar valores não inteiros')
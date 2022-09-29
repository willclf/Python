print('====>Pizzaria Wilson Gabriel de Souza<====')
print('Código |  Descrição  | Pizza Média - M | Pizza Grande – G (30% mais cara)')
print('  21   |  Napolitana |    R$ 20,00     |      R$ 26,00')
print('  22   |  Margherita |    R$ 20,00     |      R$ 26,00')
print('  23   |  Calabresa  |    R$ 25,00     |      R$ 32,50')
print('  24   |   Toscana   |    R$ 30,00     |      R$ 39,00')
print('  25   |  Portuguesa |    R$ 30,00     |      R$ 39,00')
# Tabela para facilitar o entendimento do cliente
preco = 0
qtd = 0
# para contar a quantidade de vezes que o laço foi feito e o valor total a pagar
while True:
    tamanho = input('Qual o tamanho da pizza M ou G? ')
    if tamanho.upper() == 'M': #variação de valores caso a pizza seja tamanho médio
        codigo = int(input('Digite o código do sabor: ')) #adição do codigo referente ao sabor
        if codigo == 21 or codigo == 22:
            valor = 20
        else:
            if codigo == 23:
                valor = 25
            else:
                if codigo == 24 or codigo == 25:
                    valor = 30
                else:
                    print('Operação invalida, tente novamente!')
                    continue #para retornar ao inicio do pedido

    elif tamanho.upper() == 'G': #variação de valores caso a pizza seja tamanho grande
        codigo = int(input('Digite o código do sabor: ')) #adição do codigo referente ao sabor
        if codigo == 21 or codigo == 22:
            valor = 26
        else:
            if codigo == 23:
                valor = 32.50
            else:
                if codigo == 24 or codigo == 25:
                    valor == 39
                else:
                    print('Operação invalida, tente novamente!')
                    continue #para retornar ao inicio do pedido
    else:
        print('Operação invalida, tente novamente!')
        continue #para retornar ao inicio do pedido
    preco += valor # Somatoria dos valores das pizzas
    qtd += 1 # numero de vezes que o laço foi repetido

    x = input('Gostaria de fazer mais algum pedido? ')
    if x == 'sim':
        continue #para fazer um novo pedido
    else:
        break # finaliza o laço
print('Você pediu {} pizzas e o total a pagar foi de R${:.2f}'.format(qtd, preco)) # preço final a pagar





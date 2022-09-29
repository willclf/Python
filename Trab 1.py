print('Vendas em Atacado do Wilson Gabriel de Souza!')
print('Descontos ao comprar a partir de 5 unidades')
print('Entre 5 e 19 unidades 3% de desconto')
print('Entre 20 e 99 unidades 6% de desconto')
print('Mais de 100 unidades 10% de desconto')
#Explicação para facilitar o entendimento do usuário
produto = float(input('Qual o valor do produto? ')) #Entrada do valor unitario do produto
qtd = int(input('Quantas unidade deseja? ')) #Entrada da quantidade de produtos
compra = produto * qtd
if qtd >= 100: #para compras acima de 100 unidades
    print('Valor sem desconto: R${:.2f}'.format(compra)) #demontração do valor integral
    print('Valor com desconto: R${:.2f}'.format(compra - compra*10/100)) # compra menos 10% de desconto
elif qtd >= 20: #para conpras entre 20 e 99 unidades
    print('Valor sem desconto: R${:.2f}'.format(compra)) #demontração do valor integral
    print('Valor com desconto: R${:.2f}'.format(compra - compra*6/100)) #compra menos 6% de desconto
elif qtd >= 5:
    print('Valor sem desconto: R${:.2f}'.format(compra)) #demontração do valor integral
    print('Valor com desconto: R${:.2f}'.format(compra - compra * 3 / 100)) #compra menos 3% de desconto
else:
    print('Desconto não aplicado para compras inferiores a 5 unidades')
    print('Valor a pagar: R${:.2f}'.format(compra)) #produto sem desconto
print('Volte sempre!')







km = int(input('Quantos Km foram rodados com o carro: '))
dias = int(input('Quantos dias ficou com o carro: '))
x = km * 0.15
y = dias * 60
print('O valor total do aluguel foi de: R$ {:.2f}'.format(x+y))

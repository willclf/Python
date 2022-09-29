preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual de desconto (0 a 100)%: '))
desc = preco * (p / 100)
final = preco - desc
print('O Preço do produto com desconto é: {}'.format(final))



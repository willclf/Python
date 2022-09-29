print('CALCULADORA')
print('(+) Adição')
print('(-) Subtração')
print('(*) Multiplicação')
print('(/) Divisão')
print('Pressione "s" para sair')

while True:
    op = input('qual operação deseja fazer?')
    if op == '+' or op == '-' or op == '/' or op == '*':
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))

    if op == '+':
        print('resultado é igual a: {}'.format(n1 + n2))

    elif op == '-':
        print('resultado é igual a: {}'.format(n1 - n2))

    elif op == '*':
        print('resultado é igual a: {}'.format(n1 * n2))

    elif op == '/':
        print('resultado é igual a: {}'.format(n1 / n2))

    elif (op == 's'):
        break
    else:
        print('Operação invalida')

print('Programa encerrado...')
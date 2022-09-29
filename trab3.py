print('Feijoada do Wilson Gabriel de Souza')
print('---> Volume (ml)  <--- \n \n volume < 300 Não é aceito\n 300 <= volume <= 5000 volume * 0.08 \n volume > 5000 Não é aceito\n')
#tabela para auxiliar o usuário
print('---> Tipo de Feijoada <--- \n')
print('b - Básica (Feijão + paiol +costelinha) 1.00')
print('p - Premium (Feijão + paiol +costelinha + partes de porco) 1.25')
print('s - Suprema (Feijão + paiol +costelinha + partes do porco +charque + calabresa + bacon) 1.50')

print('\n ---> Acompanhamento Valor (R$) <---\n')
print('0- Não desejo mais acompanhamentos (encerrar pedido) 0,00')
print('1- 200g de arroz 5,00')
print('2- 150g de farofa especial 6,00')
print('3- 100g de couve cozida 7,00')
print('4- 1 laranja descascada 3,00')
def volumefeijoada(): #função para definir a quantidade de feijoada desejada, e forçar o usuario a digitar corretamente a quantidade
    while True:
        try:
            volume = int(input('Digite a quantidade de ml de feijoada: '))
            if volume < 300 or volume > 5000:
                print('Consulte a tabela de volume de feijoada e tente novamente.')
                continue #caso o usuário digite um valor fora da tabela
            else:
                return volume*0.08
        except ValueError: #se o usuario digitar algum valor que nao seja um numero
            print('Pare de digitar valores não numéricos!')
def opcaofeijoada(): #função que define o tipo de feijoada
    while True:
        tipo = input('Digite tipo de feijoada (b, p, s): ')
        if tipo == 'b' or tipo == 'p' or tipo =='s':
            if tipo == 'b':
                tipo = 1
                return tipo #retorna sempre o multiplicador da feijoada
            if tipo == 'p':
                tipo = 1.25
                return tipo
            if tipo == 's':
                tipo = 1.5
                return tipo
        else:
            print('Opção invalida!')
            continue #se não for digitado o que é pedido a função retorna

def acompanhamentofeijoada(): #função dos acompanhamentos
    totalacompanhamento = 0
    while True:
        acompanhamento = input('Gostaria de algum a Companhamento\nSe sim digite o código se não digite (n): ')
        if acompanhamento == 'n': #para a função
             break

        if acompanhamento == '1':
            acompanhamento = 5
        elif acompanhamento == '2':
            acompanhamento = 6
        elif acompanhamento == '3':
            acompanhamento = 7
        elif acompanhamento == '4':
            acompanhamento = 3
        else:
            print('Opção invalida, tente novamente!') #função retorna caso usuário não digite corretamente

        totalacompanhamento += acompanhamento #soma dos acompanhamentos
        novo = input('Gostaria de mais algum acompanhamento? (s/n)')
        if novo == 's':
            continue #para fazer um novo pedido a função volta
        elif novo == 'n':
            break # para a função após apenas um pedido
        else:
            print('Opção invalida, tente novamente!')
    return totalacompanhamento
x = volumefeijoada()
y = opcaofeijoada()
z = acompanhamentofeijoada()
print('O seu pedido deu: R$ {:.2f}'.format(x * y + z)) #função final pedida pelo enunciado 

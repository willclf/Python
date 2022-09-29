l1 = int(input('Tamanho do primeiro lado do triangulo: '))
l2 = int(input('Tamanho do segundo lado do triangulo: '))
l3 = int(input('Tamanho do terceiro lado do triangulo: '))
if l1 + l2 > l3 and l3 + l2 > l1 and l1 + l3 > l2 and l1 != 0 and l2 != 0 and l3 != 0:
    if l1 == l2 == l3:
        print('É um triangulo equilátero!')
    elif l1 == l2 != l3 or l1 != l2 == l3:
        print('É um triangulo isoceles!')
    elif l1 != l2 != l3:
        print('É um triangulo escaleno!')
else:
    print('Esses valores não podem formar um triangulo!')

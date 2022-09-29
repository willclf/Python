def borda(s1):
    tam = len(s1)
    #só imprime caso exista algum caracter
    if tam:
        print('+','-' * tam,'+')
        print('|',s1,'|')
        print('+', '-' * tam, '+')

#programa principal
borda('Olá, Mundo!')
borda('Lógica de programação e algoritimos')

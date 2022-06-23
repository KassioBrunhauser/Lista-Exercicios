def pn(n):
    if n > 0:
        print('Positivo')
    elif n == 0:
        print('Nulo')
    else:
        print('Negativo')

print('positivo ou negativo')
n = int(input('digite um número: '))
print('Este número é', end=' ')
pn(n)
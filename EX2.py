lista = []
multi = 1
print()
for i in range(1,6):
    num = int(input('Digite o {}º número: '.format(i)))
    lista.append(num)
    multi = multi * num
soma = sum(lista)
print('\nOs numeros são: {}\nA soma dos numeros é: {}\nA multiplicação dos numeros é: {}'.format(lista, soma, multi))
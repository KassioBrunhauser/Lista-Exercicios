matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(" Digite o elemento: "))
print(matriz)
print('\n')

v = int(input("Digite um numero para multiplicar os elementos: "))
for i in range(3):
    for j in range(3):
        if i==j:
            matriz[i][j] = v * matriz[i][j]
print(matriz)
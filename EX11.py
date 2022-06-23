matriz1 = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        matriz1[i][j] = int(input(' Digite o elemento :'))
print(matriz1)
print('\n')
matriz2=[[0, 0], [0, 0]]
for k in range(2):
    for p in range(2):
        matriz2[k][p] = int(input('Digite o elemento:'))
print(matriz2)
print('\n')
c = [[0, 0], [0, 0]]
c[0][0]=matriz1[0][0]+matriz2[0][0]
c[1][0]=matriz1[1][0]+matriz2[1][0]
c[0][1]=matriz1[0][1]+matriz2[0][1]
c[1][1]+matriz1[1][1]+matriz2[1][1]
print('A soma das matrizes é: ', c) 
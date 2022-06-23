alunos_medias = []
alunos_media7 = 0
for i in range (10):
    somanotas = 0
    for j in range (4):
        print('Digite a:', j+1, 'º nota do ', i+1, 'º aluno', sep='')
        somanotas += float(input())
    alunos_medias.append(somanotas / 4)
    if alunos_medias [i] >= 7.0:
        alunos_media7 += 1
print("Media dos alunos:", alunos_medias)
print("Quantidade de alunos acima da media:", alunos_media7)
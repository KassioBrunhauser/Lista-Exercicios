a = []
soma = 0
for i in range(10):
    a.append(int(input("Digite um numero inteiro:")))
    soma = soma + (a[len(a) - 1] **2)
print("A soma dos quadrados do elemento do vetor sao:", soma)
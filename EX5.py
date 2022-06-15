v1 = []
v2 = []
v3 = []
for i in range(10):
    v1.append(int(input("Digite o elemento 1:")))
for i in range(10):
    v2.append(int(input("Digite o elemento 2:")))
for i in range(10):
    v3.append(v1[i])
    v3.append(v2[i])
print(v3)
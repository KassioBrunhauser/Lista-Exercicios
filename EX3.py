idades = []
altura = []
for i in range(5):
    idades.append(int(input("Digite a idade da pessoa:")))
    altura.append(float(input("Digite a altura da pessoa:")))
print("Idades na ordem inversa: ")
for i in range(5):
    print(idades[len(idades) - 1 - i])
print("Alturas na ordem inversa: ")
for i in range(5):
    print(altura[len(altura) - 1 - i])
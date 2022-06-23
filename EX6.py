frase_1 = input("Digite a frase 1:")
frase_2 = input("Digite a frase 2:")
tamanho_frase_1 = len(frase_1)
tamanho_frase_2 = len(frase_2)
print(frase_1 + " " + str(tamanho_frase_1))
print(frase_2 + " " + str(tamanho_frase_2))
if tamanho_frase_1 == tamanho_frase_2:
    print("As duas frases tem tamanhos igual")
else:
    print("As frases tem tamanhos diferentes")

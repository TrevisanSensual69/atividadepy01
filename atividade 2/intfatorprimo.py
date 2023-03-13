num = int(input("Digite um número inteiro: "))

fator = 2
while num > 1:
    if num % fator == 0:
        print(fator, end=" ")
        num /= fator
    else:
        fator += 1
print()
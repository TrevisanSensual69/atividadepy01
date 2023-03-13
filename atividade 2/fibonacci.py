num = int(input("Digite um número inteiro: "))

fibonacci = [0, 1]

if num == 1:
    print(fibonacci[0])
elif num >= 2:
    print(fibonacci[0], fibonacci[1], end=" ")
    for i in range(2, num):
        proximo = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(proximo)
        print(proximo, end=" ")
print()
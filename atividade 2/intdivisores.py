num = int(input("Digite um número inteiro: "))
print("Os divisores de", num, "são: ", end="")
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")
print()
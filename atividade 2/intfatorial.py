num = int(input("Digite um número inteiro: "))
fatorial = 1

for i in range(1, num+1):
    fatorial *= i

print(num, "! = ", fatorial)
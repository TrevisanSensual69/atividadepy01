num = int(input("Digite um número inteiro: "))
binario = ""

while num > 0:
    binario = str(num % 2) + binario
    num //= 2

print("O número em binário é: ", binario)
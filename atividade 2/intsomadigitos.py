num = int(input("Digite um número inteiro: "))
soma = 0
while num != 0:
    digito = num % 10
    soma += digito
    num = num // 10
print("A soma dos dígitos do número é:", soma)
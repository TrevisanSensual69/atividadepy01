while True:
    # Leitura do número inteiro
    num = int(input("Digite um número inteiro: "))

    # Inicialização da soma
    soma = 0

    # Cálculo da soma dos cubos dos dígitos
    temp = num
    while temp > 0:
        digito = temp % 10
        soma += digito ** 3
        temp //= 10

    # Verificação se é um número de Armstrong
    if num == soma:
        print(num, "é um número de Armstrong")
    else:
        print(num, "não é um número de Armstrong")

    # Verificação se o usuário deseja reiniciar o programa
    reiniciar = input("Deseja reiniciar o programa? (sim/não) ")
    if reiniciar.lower() != "sim":
        break

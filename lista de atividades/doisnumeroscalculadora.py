while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é igual a {resultado}.")
    elif operacao == '-':
        resultado = num1 - num2
        print(f"A subtração de {num1} por {num2} é igual a {resultado}.")
    elif operacao == '*':
        resultado = num1 * num2
        print(f"A multiplicação de {num1} por {num2} é igual a {resultado}.")
    elif operacao == '/':
        resultado = num1 / num2
        print(f"A divisão de {num1} por {num2} é igual a {resultado}.")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida (+, -, *, /).")

    continuar = input("Deseja continuar? (sim/não): ")
    if continuar.lower() != 'sim':
        break


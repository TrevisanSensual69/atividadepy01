while True:

    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    if salario <= 1500:
        aumento = salario * 0.1
    else:
        aumento = salario * 0.05
    
    novo_salario = salario + aumento

    print(f"O novo salário de {nome} é R$ {novo_salario:.2f}")
    diferenca = novo_salario - salario
    print(f"A diferença entre o salário antigo e o novo é de R$ {diferenca:.2f}")

    opcao = input("Deseja continuar? (sim/não)")
    if opcao.lower() == 'sim':
        break
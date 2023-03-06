while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print(nome + ", você é menor de idade")
    elif idade <= 65:
        print(nome + ", você é adulto")
    else:
        print(nome + ", você é idoso")
    resposta = input("Deseja verificar outra pessoa? (sim/nao): ")
    if resposta.lower() != "sim":
        break
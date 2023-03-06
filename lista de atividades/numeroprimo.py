def primo(n):
    if n < 2:  # números menores que 2 não são primos
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:  # se o número for divisível por algum número entre 2 e a raiz quadrada de n, ele não é primo
            return False
    return True  # se não houver nenhum divisor entre 2 e a raiz quadrada de n, então n é primo

while True:
    num = int(input("Digite um número inteiro: "))
    if primo(num):
        print("O número é primo.")
    else:
        print("O número não é primo.")
    resposta = input("Deseja reiniciar o programa? (sim/não): ")
    if resposta.lower() != "sim":
        break

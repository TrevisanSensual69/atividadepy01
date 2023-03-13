num = int(input("Digite um número: "))

while True:
    limit = int(input("Digite o limite da tabuada ou 0 para sair: "))
    if limit == 0:
        break
    for i in range(1, limit+1):
        print(num, "x", i, "=", num*i)
import random

dificuldade = {"Facil": 15, "Medio": 10, "Dificil": 5}

arvores = list(range(0, 49))

arvore_escondida = random.choice(arvores)

print("Escolha seu nível de dificuldade para iniciar o jogo:")
print("3 - Fácil")
print("2 - Médio")
print("1 - Difícil")
opcao = int(input("Selecione o nível: "))

tentativa = opcao * 5

while tentativa > 0:
    print("Voce possui " + str(tentativa) + " tentativa(s)")

    escolha = int(input("Escolha uma arvore: "))

    if escolha == arvore_escondida:
        print("Parabéns! Você encontrou o objeto escondido!")
        break
    elif escolha < arvore_escondida:
        print("O objeto não está na árvore selecionada. Tente uma árvore maior!")
    else:
        print("O objeto não está na árvore selecionada. Tente uma árvore menor!")

    tentativa = tentativa - 1


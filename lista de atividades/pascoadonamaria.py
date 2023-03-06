# Tamanhos dos ovos e seus respectivos preços
ovos = {"Pequeno": 7.80, "Médio": 12.90, "Grande": 23.95}

# Tipos de recheio e seus respectivos preços
recheios = {"Chocolate preto": 9.67, "Chocolate branco": 4.50, "Chocolate ao leite": 9.32}

# Adicionais e seus respectivos preços
adicionais = {"KitKat": 4.67, "MM'S": 5.43}

# Função para calcular o preço total do ovo de páscoa
def calcular_preco(tamanho, recheio, adicionais=[], quantidade=1, entrega=False, cartao=False):
    preco_base = ovos[tamanho] + recheios[recheio]
    preco_adicionais = sum([adicionais[a] for a in adicionais])
    if len(adicionais) >= 2:
        preco_adicionais *= 0.5
    if entrega:
        preco_entrega = 5.0
    else:
        preco_entrega = 0.0
    preco_total = (preco_base + preco_adicionais + preco_entrega) * quantidade
    if cartao:
        preco_total += 3.3
    else:
        preco_total *= 0.9
    return preco_total


preco_total = calcular_preco(tamanho, recheio, adicionais, quantidade, entrega, cartao)
print(f"Ovo de Páscoa {tamanho} com recheio de {recheio} e adicionais {adicionais}, quantidade: {quantidade}, entrega: {entrega}, cartão: {cartao}")
print(f"Preço total: R${preco_total:.2f}")
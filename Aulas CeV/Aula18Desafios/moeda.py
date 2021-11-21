def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    if formato == False:
        return res
    else:
        return moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    if formato == False:
        return res
    else:
        return moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    if formato == False:
        return res
    else:
        return moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    if formato == False:
        return res
    else:
        return moeda(res)


def moeda(preco=0, moeda='R$'):
    return f"{moeda}{preco:.2f}".replace(".", ",")


def resumo(preco, taxa=10, taxa2=5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"{taxa}% de aumento: \t{aumentar(preco, taxa, True)}")
    print(f"{taxa2}% de desconto: \t{diminuir(preco, taxa2, True)}")
    print("-" * 30)
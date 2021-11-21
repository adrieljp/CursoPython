def leiadinheiro(msg):
    ok = False
    while not ok:
        entrada = input(msg).replace(",", ".").strip()
        if entrada.isalpha() or entrada == '':
            print(f"\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m")
        else:
            ok = True
            return float(entrada)
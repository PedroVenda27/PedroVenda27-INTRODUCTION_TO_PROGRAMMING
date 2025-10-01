x = 1
total = 0

Depositoini = float(input("Insira o Valor referente ao deposito inicial em euros: "))
juro = float(input("Insira o Valor referente ao juros entre 0 e 100: ")) / 100

total = Depositoini

while x <= 24:
    total = total + (total * juro)
    x = x + 1
    print("VALOR DO %d mês: %.2f" % (x - 1, total))


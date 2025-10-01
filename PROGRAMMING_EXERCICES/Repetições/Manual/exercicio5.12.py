x = 1
total = 0

Depositoini = float(input("Insira o Valor referente ao deposito inicial em euros: "))
juro = float(input("Insira o Valor referente ao juros entre 0 e 100: ")) / 100

total = Depositoini


while x == 1:
    total = total + (total * juro)
    print("VALOR DO %d mês: %.2f" % (x , total))
    x = x + 1


while x <= 24:
    Depositomes = float(input("Insira o Valor extra que desja adicionar este mes: "))
    total= (total + Depositomes)
    total = total + (total * juro)
    print("VALOR DO %d mês: %.2f" % (x , total))
    x = x + 1


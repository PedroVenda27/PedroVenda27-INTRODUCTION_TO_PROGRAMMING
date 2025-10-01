y = 0
x = 1
total = 0


Divida = float(input("Insira o Valor referente a divida inicial em euros: "))
juro = float(input("Insira o Valor referente ao juros entre 0 e 100: ")) / 100

total = Divida

while x == 1:
    total = total + (total * juro)
    print("Divida do %d mês: %.2f" % (x , total))
    x = x + 1


while y <= total:
    Pagamento = float(input("Insira o Valor extra que desja adicionar este mes: "))
    total= (total - Pagamento)
    total = total + (total * juro)
    print("Divida do %d mês: %.2f" % (x , total))
    x = x + 1



print("Fim do Programa")
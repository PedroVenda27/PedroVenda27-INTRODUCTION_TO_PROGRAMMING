while True:
    divisor = int(input("Digite o divisor: "))
    dividendo= int(input("digite o dividendo: "))

    if divisor > 0 and dividendo > 0 and divisor > dividendo:
        break
    elif dividendo == 0:
        print("Aviso: Operação matematicamente indefinida!")
    else:
        print (f"{divisor} / {dividendo}: Não é possivel usar esta metodologia")



# calcular
saida = f"{divisor} / {dividendo} = "
res=0

while divisor >= dividendo:
    print (f" {divisor} - {dividendo} = {divisor - dividendo}")
    res += 1
    divisor = divisor - dividendo

saida += str(res)

print(saida)



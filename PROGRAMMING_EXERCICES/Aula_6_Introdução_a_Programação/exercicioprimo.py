#ler numero do utilizador
num = int(input ("Insira um número inteiro positivo para verificar se é primo: "))
# se o numero for menor do que 2, não pode ser primo
if num < 2:
    print (f" {num} não é primo")
else:
# verificar se o numero é primo, ou seja, se não é divisivel por
#qualquer numero entre 2 e num - 1
    for x in range (2, num):
        if num % x == 0:
            print (f" {num} não é primo, pois é divisivel por (x)")
            break
    else:
        print(f"{num} é primo")
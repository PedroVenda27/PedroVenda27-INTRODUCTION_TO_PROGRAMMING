# 11) Crie uma função que verifique se um número é primo (deverá
# retornar um valor booleano).

numero = int(input("Insira um numero para verificar se primo"))

def primo(a):

    if a < 2:
        primo = False
    else:
        for x in range (2, a):
            if a % x == 0:
                primo = False
                break
        else:
            primo = True
    return (primo)

if primo(numero):
    print("O numero inserido é primo")
else:
    print("O numero inserido não é primo")


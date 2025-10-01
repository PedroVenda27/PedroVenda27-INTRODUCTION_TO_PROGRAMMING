# 4) Crie uma função que receba um número inteiro como argumento e
# retorne o maior valor primo inferior a esse argumento. Se o
# argumento for negativo, a função deverá retornar o valor zero.  

def maior_primo_inferior_inserido(a):

    if a <= 0 :
        return 0
    
    num = 0
    while num < a:
        if num < 2:
            num = num + 1
        else:
            for x in range (2, num):
                if num % x == 0:
                    break
            else:
                primo = num
            num = num + 1
    return primo
 
print(maior_primo_inferior_inserido(10))

# 5) Crie uma função contaPrimos() que receba dois valores inteiros
# como argumentos e retorne o número de números primos entre estes
# dois números, inclusive. P. Ex. contaPrimos(3,10) deverá retornar
# o valor 3 (3, 5, 7). A função deverá ser testada sendo que os dois
# valores são introduzidos pelo utilizador. 


def contaprimos(a, b):
    primos = []
    
    for num in range(a, b + 1):
        if num < 2:
            continue
        
        eh_primo = True
        for x in range(2, num):
            if num % x == 0:
                eh_primo = False
                break
        
        if eh_primo:
            primos.append(num)

    return primos

print(contaprimos(1,10))

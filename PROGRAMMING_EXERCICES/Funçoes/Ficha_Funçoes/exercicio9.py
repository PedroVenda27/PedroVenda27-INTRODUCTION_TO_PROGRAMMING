# 9) Crie uma função que receba um número inteiro e retorne a soma
# dos seus algarismos. 

def soma_algarismos(a):
    soma = 0
    
    # Enquanto há algarismos no número
    while a > 0:
        soma = soma + (a % 10)
        a = a // 10

    return soma

print(soma_algarismos(234))
print(soma_algarismos(15))
print(soma_algarismos(9999))


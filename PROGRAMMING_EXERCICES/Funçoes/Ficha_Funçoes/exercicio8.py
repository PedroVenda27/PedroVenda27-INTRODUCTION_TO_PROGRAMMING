# 8) Crie uma função que receba um número inteiro como argumento e
# retorne o número da série de Fibonacci correspondente. 

def numerofibonacci(a):
    numeros = []
    n = 1
    A = 0 
    B = 1 
    C = 1 
    numeros.append(A)
    numeros.append(B)
    numeros.append(C)
    while n <= 100: 
        D = B + C 
        numeros.append(D)
        n = n + 1
        A, B, C = B, C, D 
    if a < 0:
        return print("introduza um valor inteiro superior a 0")
    else:
        return numeros[a]

print(numerofibonacci(7))
print(numerofibonacci(12))
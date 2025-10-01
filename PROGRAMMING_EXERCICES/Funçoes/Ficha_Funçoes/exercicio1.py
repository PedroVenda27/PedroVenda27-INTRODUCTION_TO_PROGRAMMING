# 1) Crie uma função que receba 2 valores inteiros como argumentos e
# retorne a sua soma. Se o valor da soma for negativo a função deverá
# retornar o valor 0.

def soma(a,b):
    if a + b > 0:
        return a + b
    elif a + b <= 0:
        return 0
    
print(soma(5,4))
print(soma(-5,4))
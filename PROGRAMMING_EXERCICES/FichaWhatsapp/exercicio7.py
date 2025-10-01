# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
n=1
numeros = []

while n <= 5:
        numero = int(input(f" Insira o {n}º numero: "))
        if numero < 0 :
            print("insira um valor valido")
        else:
            numeros.append(numero)
            n = n + 1

soma = sum(numeros)
print("Soma: ",soma)

multiplicacao = 1
for x in range(0, 5):
    multiplicacao = multiplicacao * numeros[x]

print( "Multiplicação: " ,multiplicacao)



# 32) Maior Sequência Crescente: Escreva um programa que leia uma
# sequência de números inteiros terminada com o número 0 (zero) e
# indique a maior sequência crescente encontrada.
 
maior_sequencia = 0
contador = 0
maior = 0
trapp = 1

while trapp == 1:

    try:
        numero = int(input("Insira um numero "))

        if numero > maior:
            contador = contador + 1

        else: 
            contador = 1

        if contador > maior_sequencia:
            maior_sequencia = contador
    
        if numero == 0: 
            trapp = 0

        maior = numero

    except ValueError:

        print("Dados inválidos!")


print("a maior sequencia de numeros crescente foi:", maior_sequencia )

    
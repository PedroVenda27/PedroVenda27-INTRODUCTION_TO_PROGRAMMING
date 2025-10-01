# 33) Sequência de Collatz: Dado um número n, a sequência de Collatz
# é obtida da seguinte forma: se n é par, divide-se por 2; se é
# ímpar, multiplica-se por 3 e soma-se 1. Repete-se o processo até
# chegar ao número 1. Escreva um programa que peça um número ao
# utilizador e mostre a sequência de Collatz correspondente.


try:
    numero = int(input("Digite um número inteiro: ")) # introduçao de um numero

    while numero != 1: # condiçao enquanto numero difrente de 1
        print(numero, end=' ') # print de um numero
        if numero % 2 == 0: # condiçao se numero par
            numero = numero // 2 # divida por 2
        
        else: # condiçao se numero nao é par
            numero = ((numero*3) + 1) # multiplique por tres 
# quando numero = 1 
    print(numero)  # print numero 1

except ValueError: # se nao for inserido um numero ou seja erro ValueError
    print("Por favor, insira um número inteiro válido.") # print mensagem e volta a pedir um numero
        
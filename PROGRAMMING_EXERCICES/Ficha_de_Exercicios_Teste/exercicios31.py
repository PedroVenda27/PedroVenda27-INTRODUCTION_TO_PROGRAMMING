# 31) Números Perfeitos: Um número é considerado perfeito se a soma
# dos seus divisores (excluindo ele mesmo) for igual ao próprio
# número. Escreva um programa que mostre todos os números perfeitos
# até 1000.

for numero in range(2, 1001): #range dos numeros que queremos verificar se sao perfeitos
    soma_divisores = 0 # variavel de controlo somoa dos divisores do numero

    for divisor in range(1, numero): # range dos divisores que de 1 a numero
        if numero % divisor == 0:  # condiçao para verificars é divisor de numero
            soma_divisores =soma_divisores + divisor # soma do divivisor a variavel soma_divisores se este verifica a condição anterior

    if soma_divisores == numero: # Condição para verificar se soma dos divisores = numero 
        print(numero) # Caso soma dos divisores = numero print do numero
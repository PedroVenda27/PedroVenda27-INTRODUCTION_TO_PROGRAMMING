# 30) Adivinhe o Número: Crie um programa onde o computador escolhe
# aleatoriamente um número entre 1 e 100. O utilizador deve tentar
# adivinhar o número. A cada tentativa, o computador indica se o
# palpite é muito alto, muito baixo ou correto


import random

numero = (random.randint(1, 100))

x=1
while x<=999:
    Tentativa = int(input("Insira um numero "))
    if Tentativa > numero:
        print("O numero que Inseriu esta a sima do numero verdadeiro")
        x=x+1
    elif Tentativa < numero:
        print("O numero que Inseriu esta a abaixo do numero verdadeiro")
        x=x+1
    else:
        print("Os numeros correspondem Parabéns voce conseguiu a" ,x, "ª tentativa")
        x=1000
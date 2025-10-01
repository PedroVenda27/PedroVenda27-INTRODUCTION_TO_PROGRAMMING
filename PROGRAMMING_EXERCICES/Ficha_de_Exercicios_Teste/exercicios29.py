# 29) Pedra, Papel, Tesoura: Escreva um programa que simule o jogo
# "Pedra, Papel, Tesoura". O utilizador deverá jogar contra o
# computador, que escolhe aleatoriamente entre as três opções. O jogo
# termina quando o utilizador decide não continuar.


import random
jogar = 0
Pedra = 1
Papel = 2
Tesoura = 3
while jogar == 0:
    print("Escolha 1 uma opção:")

    print("Pedra = 1")
    print("Papel = 2")
    print("Tesora = 3")

    utilizador = int(input("Insira o numero referente a sua escolha "))
    if utilizador == 1:
        print("Você joga Pedra")
    if utilizador == 2:
        print("Você joga Papel")
    if utilizador == 3:
        print("Você joga Tesoura")


    computador = (random.randint(1, 3))
    if computador == 1:
        print("O computador joga Pedra")
    if computador == 2:
        print("O computador joga Papel")
    if computador == 3:
        print("O computador joga Tesoura")



    if utilizador == 2 and computador == 1 or utilizador == 3 and computador == 2 or utilizador == 1 and computador == 3:
        print ("Você ganhou")

    elif utilizador == 1 and computador == 1 or utilizador == 2 and computador == 2 or utilizador == 3 and computador == 3:
        print ("Ocorre Empate")

    else:
        print ("Você perdeu")

    jogar = int(input("Insira 0 para Jogar novamente/ Insira 1 Caso não deseje jogar mais"))


print ("Fim de Programa")



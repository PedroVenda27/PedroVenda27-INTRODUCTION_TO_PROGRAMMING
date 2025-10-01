# 43) Jogo das Varetas: Simule o jogo das varetas, onde há
# inicialmente 21 varetas e os jogadores, alternadamente (utilizador
# e computador), escolhem retirar 



import random
varetas = 21
trapp = 0
while varetas>0:
    try:
        while trapp == 0:
            n=int(input("minimo (1) máximo (4) Insira o numero de Varetas a retirar:"))
            if n > 4 or n < 1:
                print(" O numero inserido deve estar entre 1 e 4")
            else:
                varetas= varetas - n 
                while trapp == 0:
                    if varetas <= 0:
                        print("Voce Perdeu")

                    else:
                        trapp=1


        while trapp==1:
            computador = (random.randint(1, 4))
            if computador == 1:
                print("O computador retira uma vareta")
            if computador == 2:
                print("O computador retira duas varetas")
            if computador == 3:
                print("O computador retira três varetas")
            if computador == 4:
                print("O computador retira quatro varetas")
            varetas=varetas-computador

            if varetas <= 0:
                print("Voce Ganhou")
                trapp = 2 
            else:
                print("restam",varetas, "varetas")
                trapp = 0

    except ValueError: # reeinserção de um numero valido caso não tenha sido inserido um numero
        print("Dados inválidos. Por favor, insira um número inteiro.") # print da mensagem para reeinserção de um numero caso o valor inserido não seja um numero



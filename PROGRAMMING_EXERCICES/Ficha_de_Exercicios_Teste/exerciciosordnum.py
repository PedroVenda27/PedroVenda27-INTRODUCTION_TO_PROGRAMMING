
trapp = 1
while trapp == 1:
    try:
        while trapp == 1:
            num1 = int(input("Insira um primeiro numero entre 0 e 9: "))
            if num1 > 9 or num1 < 0:# condição para verifiacr se o numero se encontra entre 0 e 9
                trapp = 1 # nao se encontra repete o pedido do numero
            else:
                trapp = 2 # encontra-se passa ao passo seguinte

            while trapp == 2:
                num2 = int(input("Insira um segundo numero entre 0 e 9: "))
                if num2 > 9 or num2 < 0:# condição para verifiacr se o numero se encontra entre 0 e 9
                    trapp = 2 # nao se encontra repete o pedido do numero
                else:
                    trapp = 3 # encontra-se passa ao passo seguinte

                while trapp == 3:
                    num3 = int(input("Insira um terciro numero entre 0 e 9: "))
                    if num3 > 9 or num3 < 0: # condição para verifiacr se o numero se encontra entre 0 e 9
                        trapp = 3 # nao se encontra repete o pedido do numero
                    else:
                        trapp = 4 # encontra-se passa ao passo seguinte

                    while trapp == 4:
                        num4 = int(input("Insira um quarto numero entre 0 e 9: "))
                        if num4 > 9 or num4 < 0: # condição para verifiacr se o numero se encontra entre 0 e 9
                            trapp = 4 # nao se encontra repete o pedido do numero
                        else:
                            trapp = 5 # encontra-se passa ao passo seguinte
        while trapp == 5:
            # caso num1 maior que num2 troca posiçao num1 = num2 e num2 = num1
            if num1 > num2: 
                num1,num2 = num2,num1
            # outro caso mantem
            else:
                num1 = num1
                num2 = num2
            # caso num2 maior que num3 troca posiçao num2 = num3 e num3 = num2
            if num2 > num3:
                num2,num3 = num3,num2
            # outro caso mantem
            else:
                num2 = num2
                num3 = num3
            # caso num3 maior que num4 troca posiçao num3 = num4 e num4 = num3
            if num3 > num4: 
                num3,num4 = num4,num3
            # outro caso mantem    
            else:
                num3 = num3
                num4 = num4
            # caso num1 maior que num4 troca posiçao num1 = num4 e num4 = num1
            if num1 > num4: 
                num4,num1 = num1,num4
            # outro caso mantem
            else:
                num1 = num1
                num4 = num4
            # caso num1 maior que num3 troca posiçao num1 = num3 e num3 = num1
            if num1 > num3: 
                num1,num3 = num3,num1
            # outro caso mantem
            else:
                num1 = num1
                num3 = num3
            # caso num2 maior que num4 troca posiçao num2 = num4 e num4 = num2
            if num2 > num4: 
                num2,num4 = num4,num2
            # outro caso mantem    
            else:
                num2 = num2
                num4 = num4
            # caso num1 maior que num2 troca posiçao num1 = num2 e num2 = num1
            if num1 > num2: 
                num1,num2 = num2,num1
            # outro caso mantem    
            else:
                num1 = num1
                num2 = num2
            # caso num2 maior que num3 troca posiçao num2 = num3 e num3 = num2
            if num2 > num3:
                num2,num3 = num3,num2
            # outro caso mantem    
            else:
                num2 = num2
                num3 = num3

            print(num1,num2,num3,num4)
            trapp=6

    except ValueError: # reeinserção de um numero valido caso não tenha sido inserido um numero
        print("Dados inválidos. Por favor, insira um número inteiro.") # print da mensagem para reeinserção de um numero caso o valor inserido não seja um numero



# 22) Escreva um programa em que o utilizador introduz números
# inteiros até introduzir um número em que a soma dos algarismos
# seja superior a 20.

soma = -1 # atribuição do valor -1 a variavel soma para entrada no while
while soma <= 20:
    soma = 0 # atribuição do valor o a variavel soma para inicio dos calculos
    numero = int(input("Introduza um numero: ")) # inserçao do numero que se deseja fazer asoma dos algarismo
    
    
    while numero > 0:# condição para o numero ser superior a 0 e entrada num while 
        
        alg = numero % 10 # identificação do ultimo algarismo 
        soma += alg # soma do ultimo algarismo do numero a variavel soma
        numero = numero // 10  # retirar o ultimo algarismo ao numero inserido
        # re-inicio do processo devido ao while caso numero se mantenha maior que 0
    print(soma)# print do valor da soma dos algarismos obtido
    # re-inicio do processo devido ao while caso soma seja <=20 ou finalizaçao do programa caso > 20
    

# 25) Crie um programa que imprima um número de 4 dígitos invertido
# (ex. 4536 -> 6354).
numero = int(input("Introduza o numero que deseja inverter: "))

while numero > 0:# condição para o numero ser superior a 0 e entrada num while 
        
        alg = numero % 10 # identificação do ultimo algarismo 
        numero = numero // 10  # retirar o ultimo algarismo ao numero inserido
        # re-inicio do processo devido ao while caso numero se mantenha maior que 0
        print(alg , end='')# print do valor da soma dos algarismos obtido
    # re-inicio do processo devido ao while caso soma seja <=20 ou finalizaçao do programa caso > 20
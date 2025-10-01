

trapp = 1 # Variavel de controlo para entrada no while 
resultado = 0  # Inicializa o resultado como zero para a soma começar corretamente
while trapp == 1:
    try: # tentativa de inserçao de numero inteiro
        limite = int(input("Insira o número de termos que deseja na sequência ( inteiro maior que 0): ")) # Inserir o numero máximo até qual a sequencia sera realizada
    
        if limite <= 0: # condiçao para verificar se o numero é maior que 1
            print (" O numero não corresponde as carcteristicas pedidas , Insira um número inteiro maior que 0: ")# print da mensagem para reeinserção de um novo valor caso o numero não seja maior que 1
            

        for numeroins in range(1, limite + 1): # range de 1 a limite +1 ou seja até ao verdadeiro valor do limite
            resultado = resultado + (1 / numeroins ) # formula de calculo do resultado
            print(resultado) # print do resultado
            if numeroins == limite: # condiçao para verificar se o range chegou ao fim
                trapp = 2 # quando range chega ao fim deixa de entrar no while

    except ValueError: # reeinserção de um numero valido caso não tenha sido inserido um numero
        print("Dados inválidos. Por favor, insira um número inteiro.") # print da mensagem para reeinserção de um numero caso o valor inserido não seja um numero
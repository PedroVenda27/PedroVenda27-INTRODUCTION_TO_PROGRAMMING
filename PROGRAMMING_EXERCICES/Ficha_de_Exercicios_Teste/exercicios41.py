# 41) Série Geométrica: Peça ao utilizador para inserir o primeiro
# termo, a razão e o número de termos de uma série geométrica.
# Calcule a soma dos termos dessa série.


trapp = 0 # variavel de controlo para entradada no while
while trapp == 0: # condição para se manter no while trapp ser igual a 0
    try:
        primtermo = float(input("Insira o valor do Primeiro Termo da série Geométrica: "))  # Utilizaçao de  float para aceitar números decimais / atribuiçao de valor a variavel primtermo
        razao = float(input("Insira o valor da Razão da série Geométrica: "))  # Utilizaçao de  float para aceitar números decimais / atribuiçao de valor a variavel razão
        numtermos = int(input("Insira o valor do número de termos da série Geométrica: ")) # Utilizaçao de int para aceitar apenas numeros inteiros / atribuiçao de valor a variavel numtermos
        
        if primtermo != 0 and razao != 0 and numtermos > 0:  # Verifique se o primeiro termo e a razão são diferentes de zero
            trapp = 1 #caso sejam trapp = 1 sai do while
        else:
            trapp = 0 #caso  não sejam trapp = continua no while volta a pedir os dados
            print("O primeiro termo e a razão devem ser diferentes de zero, e o número de termos deve ser maior que zero.")
    except ValueError: #caso não sinserido um valor numerico
        print("Dados inválidos. Por favor, insira um número válido.")

soma = 0 # atribuição de um valor 0 inicial a variavel de controlo soma"
contador = 0 # atribuição de um valor 0 inicial a variavel de controlo contador"

while contador < numtermos:
    termo_atual = primtermo * (razao ** contador)  # Fórmula para calcular o termo atual
    soma += termo_atual # Fórmula para adicionar o termo atual a soma dos termos
    print(f"Termo {contador + 1}: {termo_atual}") # print do termo atual
    contador += 1 # aumento de +1 no contador de termos

print("A soma dos " ,numtermos, "termos da série geométrica é:" ,soma,)
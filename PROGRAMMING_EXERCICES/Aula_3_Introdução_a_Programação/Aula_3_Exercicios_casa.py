#Exercicio 1.3.3.4 Determinar um Triangulo Válido


from math import sqrt as raizQ

# Ler as Coordenadas do Ponto 1
print("Indique as coordenadas do Ponto 1 (x1/y1)->")
x1 = int(input())
y1 = int(input())

# Ler as Coordenadas do Ponto 2
print("Indique as coordenadas do Ponto 2 (x2/y2)->")
x2 = int(input())
y2 = int(input())

# Ler as Coordenadas do Ponto 3
print("Indique as coordenadas do Ponto 3 (x3/y3)->")
x3 = int(input())
y3 = int(input())

# Calcular a medida dos lados
a = raizQ((x2 - x1)**2 + (y2 - y1))
b = raizQ((x3 - x2)**2 + (y3 - y2))
c = raizQ((x3 - x1)**2 + (y3 - y1))

# Validar triangulo de acordo com a formula

if (a < b+c) and (b < a+c) and (c < a+b):
    print("Os três pontos formam um triangulo")
else: #Caso condição anterior não aconteça
    print("Os três pontos não formam um triangulo")


# Exercicio 1.3.4.1

# Como confirmar a classificação de um triângulo atravez dos lados
# Primeiramente vamos pedir todos os lados do triângulo

lado1 = int(input("Digite o tamanho do primeiro lado: "))
lado2 = int(input("Digite o tamanho do segundo lado: "))
lado3 = int(input("Digite o tamanho do terceiro lado: "))

# Agora precisamos confirmar todos os lados, usando a fórmula do código em cima
# Caso seja difícil perceber usem o código de cima que está melhor explicado que este
# Qualquer dúvida mandem DM para __tone__ no discord

if lado1 == lado2 and lado3 < lado1:
    print("É um Triângulo Isósceles")
    print("Existe dois lados iguais e um menor.")
elif lado2 == lado3 and lado1 < lado2:
    print("É um Triângulo Isósceles")
    print("Existe dois lados iguais e um menor.")
elif lado3 == lado1 and lado2 < lado1:
    print("É um Triângulo Isósceles")
    print("Existe dois lados iguais e um menor.")
elif lado1 == lado2 and lado3:
    print("É um triângulo Equilátero")
    print("Todos os lados são iguais")
else:
    print("É um triangulo Escaleno")
    print("Todos os lados são diferentes")


# Exercicio 1.3.4.2 Divisão

# ler os numeros

print("Introduza o os valores para a sua operação")
val1= int(input("Introduza o 1º valor: ")) 
val2= int(input("Introduza o 2º valor: ")) 

# Calcular a divisão dos valores


# Classificar triangulo de acordo com o n de lados iguais
if val1==0 or val2==0:
    print("operação nao pode ser realizada")
else:
# Calcular a divisão dos valores
    divisão = (val1/val2)
    print("O valor da Divisão é:",divisão) 


# Exercioio 1.3.4.6 Determinar um ano Bissexto

# Exercicio 1.4.6 Determinar um ano
# regras
# De 4 em 4 anos é ano bissexto.
# De 100 em 100 anos não é ano bissexto.
# De 400 em 400 anos é ano bissexto.

ano = int(input("Insira um ne de um ano um ano:"))
# Agora usaremos um "if" para
# se o ano
# é divisível por 4 e por 400, ou seja se (ano % 4) e o resto for igual a e, o ano é bissexto
if (ano % 400 == 0 ) or (ano % 400 == 0 and ano % 100 != 0):
    print("o ano é Bissexto")
else:
    print("O ano é comum")
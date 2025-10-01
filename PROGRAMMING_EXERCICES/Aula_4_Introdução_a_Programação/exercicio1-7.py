# Exercicio 1

print("Insira dois nº tendo em conta que o primeiro deverá se maior que o 2º")
numero1 =int(input("insira o primeiro nº(MAIOR)"))
numero2 =int(input("insira o primeiro nº(MENOR)"))
if (numero1 % numero2 == 0 ):
    print(" O Primeiro número é multiplo do segundo")
else:
    print(" O Primeiro número não é multiplo do segundo")

# Exercicio 2 e 3 

a = int(input("Diz me um número: "))
b = int(input("Diz me um número: "))
c = int(input("Diz me um número: "))

maior = a

if a == b and a == c:
    print("Os números são iguais")
elif a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

print("O maior número é", maior)


# Exercicio 4

ano = int(input("Insira um ne de um ano um ano:"))

if (ano % 400 == 0 ) or (ano % 400 == 0 and ano % 100 != 0):
    print("o ano é Bissexto")
else:
    print("O ano é comum")


# Exercicio 5

numero = int(input("Diz me um número"))

if (numero > 999 and numero <= 9999):
    print("O número tem 4 algarismos")
else:
    print("O número não tem 4 algarismos")

# Exercicio 6

import math

# Solicite ao usuário que insira um número float
numero_float = float(input("Digite um número float: "))

# Use math.floor() para encontrar o maior inteiro que não excede o número float
numinteiro = math.floor(numero_float)

# Imprima o resultado
print("O maior inteiro que não excedente é" , numinteiro)


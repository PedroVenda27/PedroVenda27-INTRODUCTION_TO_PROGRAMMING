# Exemplo 1.1

# taxa fixa de conversão
taxa = 1.17

# ler valor em euros
Euro = int(input('Introduza valor em euros='))
ValorDollar = Euro * taxa
print("O valor em dolar é ", ValorDollar)

# Exemplo 1.2

# import math

from math import pow as elevate
from math import sqrt as raizQ


# Ler as Coordenadas do Ponto 1
print("Indique as coordenadas do Ponto 1 (x1/y1)->")
x1 = int(input())
y1 = int(input())

# Ler as Coordenadas do Ponto 2
print("Indique as coordenadas do Ponto 2 (x2/y2)->")
x2 = int(input())
y2 = int(input())

# Calcular as Distâncias elucidianas
dist = raizQ((x2 - x1)**2 + (y2 - y1)) # (x2 -X1)** <=> pow(x2 - x1, 2)

# Mostrar o Resultado
print("Distancia = %.2f" % dist) # Duas Casas Decimais


# Exemplo 1.3

#from decimal import Decimal

# Valor de Pi
pi = 3.1416

# Ler o valor do raio
print("Indique o valor do raio")
raio =  int(input())

# Calcular perimetro e área
area = (pi * (raio * raio))
perimetro = ((pi * raio)*2)

# Mostrar o Resultado
print("Area = %.4f" % area) 
print("Perimetro = %.4f" % perimetro)


# Exemplo 1.4

# Ler o valor do Cateto Oposto
print("Indique o valor do Cateto Oposto")
catop =  int(input())

# Ler o valor do Cateto Adjacente
print("Indique o valor do Cateto Adjacente")
catadj =  int(input())

# Calcular hipotenusa
hipotenusa = raizQ((catop **2)+(catadj**2) )

# Mostrar o Resultado
print("Hipotenusa = %.4f" % hipotenusa)


# Exemplo 1.5

# Ler o valor do Peso
print("Indique o Peso")
peso =  int(input())

# Ler o valor do ALTURA
print("Indique a altura")
altura =  float(input())

# Calcular hipotenusa
imc = peso/(altura * altura)

# Mostrar o Resultado do Imc
print("O seu indice de Imc é = %.4f" % imc, sep="|")



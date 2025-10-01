# 16) Escreva um programa que some os algarismos de um número.

numero = int(input("Introduza um numero: "))

soma = 0
while numero > 0:
    alg = numero % 10
    soma += alg
    numero = numero // 10

print(soma)
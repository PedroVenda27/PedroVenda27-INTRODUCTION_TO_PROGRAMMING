# Exercicio 7

# Validar triangulo de acordo com a formula 
lado1 = float(input("Digite o tamanho do primeiro lado: "))
lado2 = float(input("Digite o tamanho do segundo lado: "))
lado3 = float(input("Digite o tamanho do terceiro lado: "))


if (lado1 < lado2+lado3) and (lado2 < lado1+lado3) and (lado3 < lado1+lado2):
    print("Os três pontos formam um triangulo")
else: #Caso condição anterior não aconteça
    print("Os três pontos não formam um triangulo")


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


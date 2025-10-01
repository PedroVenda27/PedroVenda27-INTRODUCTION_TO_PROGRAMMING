# Crie um programa que leia dois ângulos de um triângulo e determine o valor do terceiro ângulo.

angulo1 = float(input("Insira a amplitude do 1º angulo"))
angulo2 = float(input("Insira a amplitude do 2º angulo"))

angulo3 = (180-angulo1-angulo2)

print ("a amplitude do terceiro angulo é" , angulo3 , "graus")
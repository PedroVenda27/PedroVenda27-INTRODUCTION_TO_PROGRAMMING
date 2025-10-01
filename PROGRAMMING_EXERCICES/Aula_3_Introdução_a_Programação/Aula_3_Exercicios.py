#sep="|"
#end=""
#"""Descrever um conjunto de notas"""





#Exercicio 1.3.2 Calcular se o aluno foi aprovado/reprovado

# ler a nota do aluno"
nota = float(input("Introduza a nota: ")) 

# Testar os casos e Mostrar o Resultado face duas situações

if nota >= 9.5:
    print("O Aluno foi aprovado")
else: #Caso condição anterior não aconteça
    print("O Aluno foi reprovado")

print("Fim")



#Exercicio 1.3.3.1 Escolher uma Letra

letra = input("Escolhe uma letra: ")

# Testar os casos e Mostrar o Resultado face duas situações

if letra == "l" or letra == "L":
    print("lIGAR")
if letra == "d" or letra == "D":
    print("Desligar")
if letra == "f" or letra == "F":
    print("Furar")
else:
    print("A Operação não pode ser feita")




#Exercicio 1.3.3.2 Verificar se Quadrado ou Retângulo e calculara a area

# ler as medidas dos lados
lado1= int(input("Introduza a medida do lado 1: ")) 
lado2= int(input("Introduza a medida do lado 2: ")) 


# Calcular a area
area = lado1 * lado2

# Testar os casos e Mostrar o Resultado face duas situações

if lado1 == lado2:
    print("A area do quadrado:",area)
else:
    print("A area do retagulo:",area)  

#Exercicio 1.3.3.3 Determinar o maximo da Três Valores

# ler os numeros
num1= int(input("Introduza o 1º numero: ")) 
num2= int(input("Introduza o 2º numero: ")) 
num3= int(input("Introduza o 3º numero: ")) 

# Testar os casos e Mostrar o Resultado face as duas situações (são todos iguais) ou (exite um maior)
if num1 > num2 and num1 > num3:
    print("O maior valor é",num1)
elif num2 > num1 and num2 > num3:
    print('O maior numero é',num2)
elif num3 > num2 and num3 > num1:
    print('O maior numero é',num3)
else:
 print("erro")   







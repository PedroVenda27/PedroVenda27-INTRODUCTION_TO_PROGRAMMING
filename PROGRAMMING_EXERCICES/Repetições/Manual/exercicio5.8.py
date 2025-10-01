#Exercicio 5.8
numero1 = int(input("Insira um Numero"))
numero2 = int(input("Inseira o N por qual deseja multiplicar o n anterior"))
print (numero1,"x",numero2,"=",numero1*numero2,end = " " "= ")

x=0
while x<=numero2:
    print ( numero1,"+",end = " ")
    x=x+1

print("=", end = " ")

x=0
while x<=numero1:
 if x < numero1:
    print (numero2,"+", end = " ")
    x=x+1
 else:
    print (numero2)
    x=x+1       
    
print("Fim do Programa")
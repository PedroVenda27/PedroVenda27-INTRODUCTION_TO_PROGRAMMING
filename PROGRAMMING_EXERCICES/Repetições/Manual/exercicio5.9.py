#Exercicio 5.9
total=0


numero1 = int(input("Insira um Numero:"))
numero2 = int(input("Inseira o N por qual deseja dividir o n anterior:"))

res=0
x=0
while x==0:
    resto=(numero1-numero2)
    res=res+1
    x=x+1

while resto>=numero2:
    resto=(resto-numero2)
    res=res+1

print(numero1 ,"a dividir por", numero2) 
print("É Possivivel dividir" , res ,"Vezes e tem resto" , resto)
  
print("Fim do Programa")
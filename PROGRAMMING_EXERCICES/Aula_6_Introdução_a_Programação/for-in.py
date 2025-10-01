#Explicaçaão do For In

num1 = num2 = 0 #cair no while

while num1 == num2: # inserir dois numeros 
    num1 = int(input( "Introzuma o numero 1 ->"))
    num2 = int(input("Introduza o numero 2 -> "))

#determinar minimo e maximo
minimo = min (num1, num2)
maximo = max (num1, num2)


somar = 0 #

intervalo = int(input("Introduza o intervalo -> "))


for x in range (minimo, maximo + 1, intervalo):
    somar += x
    print (f"x: {x}")

print (f"Soma: {somar}")

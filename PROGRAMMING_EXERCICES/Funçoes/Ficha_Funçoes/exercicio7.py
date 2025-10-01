# 7) Crie uma função que receba dois valores inteiros como argumentos
# e retorne um valor booleano indicando se os números são divisíveis. 

def divisaorestozero(a,b):
    possivel = True

    if a > 0 and b > 0 and a > b:
     maximo = a
     minimo = b

    if a > 0 and b > 0 and b > a:
     maximo = b
     minimo = a

    if maximo % minimo != 0:
      possivel = False

    return possivel

if (divisaorestozero(8,3)):
    print("Possivel dividir")
else:
    print("Impossivel dividir com resto 0")

if (divisaorestozero(6,3)):
    print("Possivel dividir")
else:
    print("Impossivel dividir com resto 0")






    

   


    





































































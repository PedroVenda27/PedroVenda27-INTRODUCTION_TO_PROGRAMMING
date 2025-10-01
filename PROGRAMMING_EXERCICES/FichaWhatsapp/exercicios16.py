# Utilize uma lista para resolver o problema a seguir. 
# Uma empresa paga seus vendedores com base em comissões. 
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante

n = 1
vendas = []

intervalo1 = []
intervalo2 = []
intervalo3 = []
intervalo4 = []
intervalo5 = []
intervalo6 = []
intervalo7 = []
intervalo8 = []
intervalo9 = []




while n <= 10:
        valor_vendas = int(input(f" Insira o valor das vendas do vendedor {n}: "))
        if valor_vendas <= 0:
            print("Puto tas despedido")
        else:
            vendas.append(valor_vendas)
            n = n + 1

for num in vendas:
     salario = 200 +(0.09 * num)
     if salario >= 200 and salario <= 299:
          intervalo1.append(num)
     if salario >= 300 and salario <= 399:
          intervalo2.append(num)
     if salario >= 400 and salario <= 499:
          intervalo3.append(num)
     if salario >= 500 and salario <= 599:
          intervalo4.append(num)
     if salario >= 600 and salario <= 699:
          intervalo5.append(num)
     if salario >= 700 and salario <= 799:
          intervalo6.append(num)
     if salario >= 800 and salario <= 899:
          intervalo7.append(num)
     if salario >= 900 and salario <= 899:
          intervalo8.append(num)
     if salario >= 1000:
          intervalo9.append(num)
          

print("Numero de Salarios entregues no intervalo de 200$-299$", len(intervalo1))
print("Valores Entregues", intervalo1)

print("Numero de Salarios entregues no intervalo de 300$-399$", len(intervalo2))
print("Valores Entregues", intervalo2)

print("Numero de Salarios entregues no intervalo de 400$-499$", len(intervalo3))
print("Valores Entregues", intervalo3)

print("Numero de Salarios entregues no intervalo de 500$-599$", len(intervalo4))
print("Valores Entregues", intervalo4)

print("Numero de Salarios entregues no intervalo de 600$-699$", len(intervalo5))
print("Valores Entregues", intervalo5)

print("Numero de Salarios entregues no intervalo de 700$-799$", len(intervalo6))
print("Valores Entregues", intervalo6)

print("Numero de Salarios entregues no intervalo de 800$-899$", len(intervalo7))
print("Valores Entregues", intervalo7)

print("Numero de Salarios entregues no intervalo de 900$-999$", len(intervalo8))
print("Valores Entregues", intervalo8)

print("Numero de Salarios entregues no intervalo de 1000$-", len(intervalo9))
print("Valores Entregues", intervalo9)      

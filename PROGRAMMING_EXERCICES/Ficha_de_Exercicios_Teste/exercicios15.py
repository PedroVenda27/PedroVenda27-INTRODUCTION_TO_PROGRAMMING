# 5) Escreva um programa que calcule o fatorial de um número.

num = -1

while num < 0:
    num = int(input("Diz me um número entre para realizar o seu fatorial: "))
fatorial = 1

if num == 0:
    print('Fatorial de', num, "é 0")
else: 
    for i in range(num, 0, -1):
       fatorial *=  i

print(f"O fatorial de {num} é {fatorial}")
num = -1

while num < 0 or num >= 10:
    num = int(input("Diz me um número entre 1 - 10 para realizar o seu fatorial: "))
fatorial = 1

if num == 0:
    print('Fatorial de', num, "é 0")
else: 
    for i in range(num, 0, -1):
       fatorial *=  i

print(f"O fatorial de {num} é {fatorial}")
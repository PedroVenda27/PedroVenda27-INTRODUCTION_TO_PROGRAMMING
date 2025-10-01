# 16) Crie um programa que conte o número de números primos num
# vetor de inteiros. 


vetor = []
n=1
while True:
    valor = int(input(f"(insira 0 caso deseje terminar) Introduza o {n}º valor a colocar no vetor: "))
    if valor == 0:
        break
    if valor < 0:
        print("insira um valor inteiro positivo")
    if valor >= 1:
        vetor.append(valor)
        n=n+1

print(vetor)


numprimos = 0

for num in vetor:
    if num > 1:  # 1 não é primo, então pulamos
        e_primo = True
        for i in range(2, num):
            if (num % i) == 0:
                e_primo = False
                break
        if e_primo:
            numprimos += 1

print ("Total de Numeros Primos:",(numprimos))

